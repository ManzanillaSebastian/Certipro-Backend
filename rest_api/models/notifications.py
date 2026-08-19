"""Notifications module"""

from django.conf import settings
from django.db import models

from .feedbacks import Feedback
from .uploaded_evidences import UploadedEvidence


class NotificationType(models.TextChoices):
    """The kind of event a notification represents"""

    EVIDENCE_REJECTED = "EVIDENCE_REJECTED", "Evidence Rejected"


class Notification(models.Model):
    """
    Represents an in-system notification delivered to a user, for example
    to let a Member know that an uploaded evidence was reviewed and
    rejected by a supervisor.
    """

    notification_type = models.CharField(
        max_length=30,
        choices=NotificationType.choices,
        default=NotificationType.EVIDENCE_REJECTED,
    )

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # The user who should see this notification
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    # Optional link back to the evidence that triggered the notification
    uploaded_evidence = models.ForeignKey(
        UploadedEvidence,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
    )

    # Optional link back to the feedback that triggered the notification
    feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Notification for {self.recipient} ({self.notification_type})"
