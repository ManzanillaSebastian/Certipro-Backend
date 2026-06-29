"""View for CRUD operations on the uploaded_evidences table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.uploaded_evidences import UploadedEvidence
from ..serializers.uploaded_evidences import UploadedEvidenceSerializer


class UploadedEvidenceViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for handling documents uploaded to fulfill tasks.
    """

    queryset = UploadedEvidence.objects.all().order_by("-uploaded_at")
    serializer_class = UploadedEvidenceSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = [
        "id",
        "file_path",
        "description",
        "uploaded_at",
        "task",
        "required_evidence",
    ]
