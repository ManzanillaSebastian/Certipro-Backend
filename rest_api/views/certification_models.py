"""View for CRUD operations on certification_models table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.certification_models import CertificationModel
from ..serializers.certification_models import CertificationModelSerializer
from .filter_mixins import QueryParamFilterMixin


class CertificationModelViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing certification models.
    Requires JWT authentication to ensure secure data access.
    """

    queryset = CertificationModel.objects.all().order_by("-start_date")
    serializer_class = CertificationModelSerializer
    permission_classes = [IsAuthenticated]  # JWT
    allowed_filters = ["id", "title", "accreditor", "start_date", "end_date"]
