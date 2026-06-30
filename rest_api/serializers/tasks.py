"""Serializer for CRUD operations on the tasks table"""

from rest_framework import serializers

from ..models.tasks import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer to map task assignments for work groups.
    """

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "criterion",
            "requirement_version",
            "group_responsible",
        ]
