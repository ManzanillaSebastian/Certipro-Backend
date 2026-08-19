"""Serializer for CRUD operations on the notifications table"""

from rest_framework import serializers

from ..models.notifications import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer used by a user to read and acknowledge their own
    in-system notifications (e.g. an evidence rejection alert).
    """

    task_title = serializers.CharField(
        source="uploaded_evidence.task.title", read_only=True, default=None
    )
    required_evidence_title = serializers.CharField(
        source="uploaded_evidence.required_evidence.title",
        read_only=True,
        default=None,
    )

    class Meta:
        model = Notification
        fields = [
            "id",
            "notification_type",
            "message",
            "is_read",
            "created_at",
            "recipient",
            "uploaded_evidence",
            "feedback",
            "task_title",
            "required_evidence_title",
        ]
        read_only_fields = [
            "id",
            "notification_type",
            "message",
            "created_at",
            "recipient",
            "uploaded_evidence",
            "feedback",
        ]
