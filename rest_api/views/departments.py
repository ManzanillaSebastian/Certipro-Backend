"""View for CRUD operations on the departments table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.departments import Department
from ..serializers.departments import DepartmentSerializer
from .filter_mixins import QueryParamFilterMixin


class DepartmentViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing branch departments.
    """

    queryset = Department.objects.all().order_by("name")
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ["id", "name", "branch", "supervisor"]
