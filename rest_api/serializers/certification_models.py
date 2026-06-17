"""Serializer for CRUD operations on certification_models table"""
from rest_framework import serializers
from ..models.certification_models import CertificationModel

class CertificationModelSerializer(serializers.ModelSerializer):
    """
    Serializer to map the CertificationModel data to and from JSON.
    """
    class Meta:
        model = CertificationModel
        fields = ['id', 'title', 'accreditor', 'start_date', 'end_date']
