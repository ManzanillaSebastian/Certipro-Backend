"""All urls available for api requests"""
# rest_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Routers
router = DefaultRouter()
router.register(r'certification_models', CertificationModelViewSet, basename='certification_model')
router.register(r'periods', PeriodViewSet, basename='period')
router.register(r'criteria', CriterionViewSet, basename='criterion')
router.register(r'requirements', RequirementViewSet, basename='requirement')
router.register(r'requirement_versions', RequirementVersionViewSet, basename='requirement_version')
router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'work_groups', WorkGroupViewSet, basename='work_group')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'required_evidences', RequiredEvidenceViewSet, basename='required_evidence')
router.register(r'uploaded_evidences', UploadedEvidenceViewSet, basename='uploaded_evidence')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]