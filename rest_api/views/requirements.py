"""View for CRUD operations on the requirements table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.requirements import Requirement, RequirementVersion
from ..serializers.requirements import RequirementSerializer, RequirementVersionSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage the global catalog of reusable requirements.
    """
    queryset = Requirement.objects.all().order_by('id')
    serializer_class = RequirementSerializer
    permission_classes = [IsAuthenticated]


class RequirementVersionViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage specific versions of global requirements.
    """
    queryset = RequirementVersion.objects.all()
    serializer_class = RequirementVersionSerializer
    permission_classes = [IsAuthenticated]
