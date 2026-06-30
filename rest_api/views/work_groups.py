"""View for CRUD operations on the work_groups table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.work_groups import WorkGroup
from ..serializers.work_groups import WorkGroupSerializer
from .filter_mixins import QueryParamFilterMixin


class WorkGroupViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing work groups and team rosters.
    """

    queryset = WorkGroup.objects.all().order_by("name")
    serializer_class = WorkGroupSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ["id", "name", "department", "supervisor", "members"]
