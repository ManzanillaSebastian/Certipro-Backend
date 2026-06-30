"""Serializer for CRUD operations on the requirements table"""

from rest_framework import serializers

from ..models.requirements import Requirement, RequirementVersion


class RequirementVersionSerializer(serializers.ModelSerializer):
    """
    Serializer to handle version logs for each global requirement.
    """

    class Meta:
        model = RequirementVersion
        fields = ["id", "requirement", "version_number", "is_active", "created_at"]


class RequirementSerializer(serializers.ModelSerializer):
    """
    Serializer to map global requirements, including all their version history.
    """

    # 💡 Esto permite ver la lista de versiones anidadas al hacer un GET
    versions = RequirementVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Requirement
        fields = ["id", "title", "description", "versions"]
