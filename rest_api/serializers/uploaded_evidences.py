"""Serializer for CRUD operations on the uploaded_evidences table"""
from rest_framework import serializers
from ..models.uploaded_evidences import UploadedEvidence

class UploadedEvidenceSerializer(serializers.ModelSerializer):
    """
    Serializer to handle physical file uploads and linking them to task slots.
    """
    class Meta:
        model = UploadedEvidence
        fields = ['id', 'file_path', 'description', 'uploaded_at', 'task', 'required_evidence']