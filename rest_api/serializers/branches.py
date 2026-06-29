"""Serializer for CRUD operations on the branches table"""

from rest_framework import serializers
from ..models.branches import Branch


class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer to map Branch organizational units.
    """

    class Meta:
        model = Branch
        fields = ["id", "name", "location", "supervisor"]
