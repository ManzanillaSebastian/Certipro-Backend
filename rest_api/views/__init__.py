from .authentication import LoginView as LoginView
from .branches import BranchViewSet as BranchViewSet
from .certification_models import CertificationModelViewSet as CertificationModelViewSet
from .criteria import CriterionViewSet as CriterionViewSet
from .departments import DepartmentViewSet as DepartmentViewSet
from .feedbacks import FeedbackViewSet as FeedbackViewSet
from .notifications import NotificationViewSet as NotificationViewSet
from .periods import PeriodViewSet as PeriodViewSet
from .required_evidences import RequiredEvidenceViewSet as RequiredEvidenceViewSet
from .requirements import (
    RequirementVersionViewSet as RequirementVersionViewSet,
)
from .requirements import (
    RequirementViewSet as RequirementViewSet,
)
from .tasks import TaskViewSet as TaskViewSet
from .uploaded_evidences import UploadedEvidenceViewSet as UploadedEvidenceViewSet
from .users import UserViewSet as UserViewSet
from .work_group_members import WorkGroupMemberViewSet as WorkGroupMemberViewSet
from .work_groups import WorkGroupViewSet as WorkGroupViewSet
