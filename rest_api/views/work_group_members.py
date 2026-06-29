"""View for CRUD operations on the work group members through table."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.work_groups import WorkGroup
from ..serializers.work_group_members import WorkGroupMemberSerializer


class WorkGroupMemberViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for managing the automatic many-to-many records linking work groups and users.
    """

    queryset = WorkGroup.members.through.objects.all()
    serializer_class = WorkGroupMemberSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ["id", "workgroup", "user"]
