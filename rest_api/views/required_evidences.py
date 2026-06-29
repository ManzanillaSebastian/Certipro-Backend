"""View for CRUD operations on the required_evidences table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.required_evidences import RequiredEvidence
from ..serializers.required_evidences import RequiredEvidenceSerializer


class RequiredEvidenceViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for tracking rules governing expected digital assets.
    """

    queryset = RequiredEvidence.objects.all()
    serializer_class = RequiredEvidenceSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ["id", "title", "description", "file_type", "requirement_version"]
