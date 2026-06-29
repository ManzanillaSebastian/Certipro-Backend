from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

from .models import (
    Branch as Branch,
    CertificationModel as CertificationModel,
    Criterion as Criterion,
    CriterionPriority as CriterionPriority,
    Department as Department,
    Feedback as Feedback,
    FeedbackResult as FeedbackResult,
    Period as Period,
    Requirement as Requirement,
    RequiredEvidence as RequiredEvidence,
    RequirementVersion as RequirementVersion,
    Task as Task,
    UploadedEvidence as UploadedEvidence,
    User as User,
    UserRole as UserRole,
    WorkGroup as WorkGroup,
)


class CertiProModelTestCase(TestCase):
    def setUp(self):
        """
        Inyección de dependencias base necesarias para poblar las relaciones externas.
        """
        # Base de usuarios con roles diferenciados
        self.admin_user = User.objects.create_user(
            username="admin_test",
            email="admin@certipro.com",
            password="pwd",
            role="ADMINISTRADOR",
        )
        self.supervisor_user = User.objects.create_user(
            username="super_test",
            email="super@certipro.com",
            password="pwd",
            role="SUPERVISOR",
        )
        self.member_user = User.objects.create_user(
            username="member_test",
            email="member@certipro.com",
            password="pwd",
            role="MIEMBRO DE EQUIPO",
        )

        # Entidades globales transversales
        self.cert_model = CertificationModel.objects.create(
            title="Modelo de Evaluación 2026",
            accreditor="CACES",
            start_date=date(2026, 1, 1),
            end_date=date(2026, 12, 31),
        )

        self.requirement = Requirement.objects.create(
            title="Silabo de Materia", description="Estructura curricular de la materia"
        )

        self.req_version = RequirementVersion.objects.create(
            requirement=self.requirement, version_number="v1.0", is_active=True
        )

    # 1. TEST: User Model
    def test_user_creation_and_role_default(self):
        """Valida que un usuario se guarde correctamente y aplique el rol MEMBER por defecto."""
        user = User.objects.create_user(
            username="default_user",
            email="default@certipro.com",
            password="password123",
        )
        self.assertEqual(user.role, "MIEMBRO DE EQUIPO")
        self.assertEqual(user.USERNAME_FIELD, "email")

    # 2. TEST: Branch Model
    def test_branch_creation_with_supervisor(self):
        """Verifica la asignación de sedes organizacionales y su supervisor jerárquico."""
        branch = Branch.objects.create(
            name="Campus Prosperina",
            location="Km 30.5 Vía Perimetral",
            supervisor=self.supervisor_user,
        )
        self.assertEqual(branch.supervisor.role, "SUPERVISOR")
        self.assertIn(branch, self.supervisor_user.supervised_branches.all())

    # 3. TEST: Department Model
    def test_department_cascade_deletion(self):
        """Valida la restricción CASCADE: Si la sede se elimina, el departamento se va con ella."""
        branch = Branch.objects.create(name="Sede Temporal")
        dept = Department.objects.create(name="FIMCP", branch=branch)

        branch.delete()
        self.assertFalse(Department.objects.filter(id=dept.id).exists())

    # 4. TEST: WorkGroup Model
    def test_work_group_many_to_many_members(self):
        """Prueba la asignación de múltiples miembros operativos a un equipo de trabajo."""
        branch = Branch.objects.create(name="Sede Norte")
        dept = Department.objects.create(name="FIEC", branch=branch)
        group = WorkGroup.objects.create(
            name="Célula de Desarrollo Backend", department=dept
        )

        group.members.add(self.member_user)
        self.assertIn(self.member_user, group.members.all())
        self.assertIn(group, self.member_user.work_groups_joined.all())

    # 5. TEST: CertificationModel
    def test_certification_model_attributes(self):
        """Valida el almacenamiento de los metadatos de un modelo evaluativo internacional o nacional."""
        self.assertEqual(self.cert_model.accreditor, "CACES")
        self.assertTrue(self.cert_model.end_date > self.cert_model.start_date)

    # 6. TEST: Criterion Model
    def test_criterion_recursive_tree_structure(self):
        """Valida la recursividad jerárquica: Un criterio puede albergar subcriterios hijos."""
        parent_criterion = Criterion.objects.create(
            code="CRIT-1",
            title="Docencia",
            priority=CriterionPriority.HIGH,
            certification_model=self.cert_model,
        )
        sub_criterion = Criterion.objects.create(
            code="SUB-1.1",
            title="Gestión de Aprendizaje",
            priority=CriterionPriority.MEDIUM,
            certification_model=self.cert_model,
            parent=parent_criterion,
        )
        self.assertEqual(sub_criterion.parent, parent_criterion)
        self.assertIn(sub_criterion, parent_criterion.subcriteria.all())

    # 7. TEST: Period Model
    def test_period_temporal_lock_default(self):
        """Verifica que los bloques de control temporal permitan modificaciones del sistema por defecto."""
        period = Period.objects.create(
            name="Fase de Autoevaluación Inicial",
            start_date=date(2026, 2, 1),
            end_date=date(2026, 3, 1),
            certification_model=self.cert_model,
        )
        self.assertTrue(period.allow_editing)

    # 8. TEST: Requirement & RequirementVersion Models
    def test_requirement_string_representation(self):
        """Asegura que el catálogo global implemente de forma limpia su método str corporativo."""
        self.assertEqual(str(self.requirement), "Silabo de Materia")

    # 9. TEST: RequiredEvidence Model
    def test_required_evidence_slots(self):
        """Garantiza la definición estricta de las extensiones esperadas en la plantilla."""
        evidence_slot = RequiredEvidence.objects.create(
            title="PDF de Planificación Integrada",
            file_type=".pdf",
            requirement_version=self.req_version,
        )
        self.assertEqual(evidence_slot.file_type, ".pdf")

    # 10. TEST: Task Model
    def test_task_integrity_protection_on_delete(self):
        """Prueba crítica de negocio: Evita la eliminación de un grupo si mantiene tareas activas."""
        branch = Branch.objects.create(name="Sede Central")
        dept = Department.objects.create(name="Ventas", branch=branch)
        group = WorkGroup.objects.create(name="Equipo de Carga", department=dept)

        criterion = Criterion.objects.create(
            code="C2", title="Infra", certification_model=self.cert_model
        )

        Task.objects.create(
            title="Subir planos",
            start_date=date(2026, 6, 1),
            end_date=date(2026, 7, 1),
            criterion=criterion,
            requirement_version=self.req_version,
            group_responsible=group,
        )

        # Debe lanzar un error de protección y denegar el borrado del grupo responsable
        with self.assertRaises(IntegrityError):
            group.delete()

    # 11. TEST: UploadedEvidence Model
    def test_uploaded_evidence_association(self):
        """Simula la subida física de un documento digital enlazándolo a su slot e hito correspondiente."""
        branch = Branch.objects.create(name="Sede Central")
        dept = Department.objects.create(name="Admin", branch=branch)
        group = WorkGroup.objects.create(name="Equipo G1", department=dept)
        criterion = Criterion.objects.create(
            code="C3", title="Evidencias", certification_model=self.cert_model
        )

        task = Task.objects.create(
            title="Subida Obligatoria",
            start_date=date(2026, 6, 1),
            end_date=date(2026, 7, 1),
            criterion=criterion,
            requirement_version=self.req_version,
            group_responsible=group,
        )
        slot = RequiredEvidence.objects.create(
            title="Slot 1", file_type=".png", requirement_version=self.req_version
        )

        fake_file = SimpleUploadedFile(
            "evidencia_firmada.png", b"file_content", content_type="image/png"
        )
        uploaded = UploadedEvidence.objects.create(
            file_path=fake_file,
            description="Planos validados finales",
            task=task,
            required_evidence=slot,
        )
        self.assertIn(uploaded, task.uploaded_evidences.all())

    # 12. TEST: Feedback Model
    def test_feedback_evaluator_and_result(self):
        """Valida que una revisión almacene correctamente la aprobación o el rechazo de evidencias."""
        branch = Branch.objects.create(name="Sede Central")
        dept = Department.objects.create(name="Calidad", branch=branch)
        group = WorkGroup.objects.create(name="Auditores", department=dept)
        criterion = Criterion.objects.create(
            code="C4", title="Auditoría", certification_model=self.cert_model
        )

        task = Task.objects.create(
            title="Carga de Informes",
            start_date=date(2026, 6, 1),
            end_date=date(2026, 7, 1),
            criterion=criterion,
            requirement_version=self.req_version,
            group_responsible=group,
        )
        slot = RequiredEvidence.objects.create(
            title="Informe General",
            file_type=".docx",
            requirement_version=self.req_version,
        )

        fake_file = SimpleUploadedFile(
            "informe.docx", b"data", content_type="application/msword"
        )
        evidence = UploadedEvidence.objects.create(
            file_path=fake_file, task=task, required_evidence=slot
        )

        feedback = Feedback.objects.create(
            comment="El documento cumple con todos los estándares e indicadores exigidos.",
            result_type=FeedbackResult.APPROVE,
            uploaded_evidence=evidence,
            evaluator=self.supervisor_user,
        )
        self.assertEqual(feedback.result_type, "APPROVE")
        self.assertEqual(feedback.evaluator, self.supervisor_user)
