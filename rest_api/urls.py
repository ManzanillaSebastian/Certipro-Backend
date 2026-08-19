"""All urls available for api requests"""

# rest_api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BranchViewSet as BranchViewSet,
)
from .views import (
    CertificationModelViewSet as CertificationModelViewSet,
)
from .views import (
    CriterionViewSet as CriterionViewSet,
)
from .views import (
    DepartmentViewSet as DepartmentViewSet,
)
from .views import (
    FeedbackViewSet as FeedbackViewSet,
)
from .views import (
    LoginView as LoginView,
)
from .views import (
    NotificationViewSet as NotificationViewSet,
)
from .views import (
    PeriodViewSet as PeriodViewSet,
)
from .views import (
    RequiredEvidenceViewSet as RequiredEvidenceViewSet,
)
from .views import (
    RequirementVersionViewSet as RequirementVersionViewSet,
)
from .views import (
    RequirementViewSet as RequirementViewSet,
)
from .views import (
    TaskViewSet as TaskViewSet,
)
from .views import (
    UploadedEvidenceViewSet as UploadedEvidenceViewSet,
)
from .views import (
    UserViewSet as UserViewSet,
)
from .views import (
    WorkGroupMemberViewSet as WorkGroupMemberViewSet,
)
from .views import (
    WorkGroupViewSet as WorkGroupViewSet,
)

# Routers
router = DefaultRouter()
router.register(
    r"certification_models", CertificationModelViewSet, basename="certification_model"
)
router.register(r"periods", PeriodViewSet, basename="period")
router.register(r"criteria", CriterionViewSet, basename="criterion")
router.register(r"requirements", RequirementViewSet, basename="requirement")
router.register(
    r"requirement_versions", RequirementVersionViewSet, basename="requirement_version"
)
router.register(r"branches", BranchViewSet, basename="branch")
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"work_groups", WorkGroupViewSet, basename="work_group")
router.register(
    r"work_group_members", WorkGroupMemberViewSet, basename="work_group_member"
)
router.register(r"tasks", TaskViewSet, basename="task")
router.register(
    r"required_evidences", RequiredEvidenceViewSet, basename="required_evidence"
)
router.register(
    r"uploaded_evidences", UploadedEvidenceViewSet, basename="uploaded_evidence"
)
router.register(r"feedbacks", FeedbackViewSet, basename="feedback")
router.register(r"notifications", NotificationViewSet, basename="notification")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
