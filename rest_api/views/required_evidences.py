"""View for CRUD operations on the required_evidences table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.required_evidences import RequiredEvidence
from ..serializers.required_evidences import RequiredEvidenceSerializer

class RequiredEvidenceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for tracking rules governing expected digital assets.
    """
    queryset = RequiredEvidence.objects.all()
    serializer_class = RequiredEvidenceSerializer
    permission_classes = [IsAuthenticated]