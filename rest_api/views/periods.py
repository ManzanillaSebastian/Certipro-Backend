"""View for CRUD operations on periods table"""
# rest_api/views/periods.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.periods import Period
from ..serializers.periods import PeriodSerializer

class PeriodViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing evaluation periods.
    """
    queryset = Period.objects.all().order_by('start_date')
    serializer_class = PeriodSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ['id', 'name', 'reason', 'allow_editing', 'start_date', 'end_date', 'certification_model']
