"""Serializer for CRUD operations on the departments table"""
from rest_framework import serializers
from ..models.departments import Department

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer to map internal departments within branches.
    """
    class Meta:
        model = Department
        fields = ['id', 'name', 'branch', 'supervisor']