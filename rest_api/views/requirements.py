"""View for CRUD operations on the requirements table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.requirements import Requirement, RequirementVersion
from ..serializers.requirements import RequirementSerializer, RequirementVersionSerializer
from .filter_mixins import QueryParamFilterMixin

class RequirementViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet to manage the global catalog of reusable requirements.
    """
    queryset = Requirement.objects.all().order_by('id')
    serializer_class = RequirementSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ['id', 'title', 'description']


class RequirementVersionViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet to manage specific versions of global requirements.
    """
    queryset = RequirementVersion.objects.all()
    serializer_class = RequirementVersionSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ['id', 'requirement', 'version_number', 'is_active', 'created_at']
