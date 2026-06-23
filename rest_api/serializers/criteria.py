"""Serializer for CRUD operations on the criteria table"""
from rest_framework import serializers
from ..models.criteria import Criterion

class CriterionSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Criterion data to and from JSON.
    Supports hierarchical tree structure listing through the parent ID.
    """
    class Meta:
        model = Criterion
        fields = ['id', 'priority', 'code', 'title', 'description', 'certification_model', 'parent']