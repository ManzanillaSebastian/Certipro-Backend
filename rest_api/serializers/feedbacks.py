"""Serializer for CRUD operations on the feedbacks table"""
from rest_framework import serializers
from ..models.feedbacks import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for supervisors to audit and log feedback on uploaded documents.
    """
    class Meta:
        model = Feedback
        fields = ['id', 'comment', 'result_type', 'reviewed_at', 'uploaded_evidence', 'evaluator']