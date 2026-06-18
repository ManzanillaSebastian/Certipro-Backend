"""Serializer for CRUD operations on the required_evidences table"""
from rest_framework import serializers
from ..models.required_evidences import RequiredEvidence

class RequiredEvidenceSerializer(serializers.ModelSerializer):
    """
    Serializer to define expected template slots for evidence submission.
    """
    class Meta:
        model = RequiredEvidence
        fields = ['id', 'title', 'description', 'file_type', 'requirement_version']