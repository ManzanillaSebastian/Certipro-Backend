"""Serializer for CRUD operations on the work_groups table"""

from rest_framework import serializers
from ..models.work_groups import WorkGroup


class WorkGroupSerializer(serializers.ModelSerializer):
    """
    Serializer to map specific work teams, including their supervisor and member lists.
    """

    class Meta:
        model = WorkGroup
        fields = ["id", "name", "department", "supervisor", "members"]
