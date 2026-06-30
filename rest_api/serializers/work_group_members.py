"""Serializer for CRUD operations on the work group members through table."""

from rest_framework import serializers

from ..models.work_groups import WorkGroup


class WorkGroupMemberSerializer(serializers.ModelSerializer):
    """
    Serializer to expose the automatic many-to-many relation between work groups and users.
    """

    class Meta:
        model = WorkGroup.members.through
        fields = ["id", "workgroup", "user"]
