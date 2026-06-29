"""Feedbacks module"""

from django.db import models
from django.conf import settings
from .uploaded_evidences import UploadedEvidence


class FeedbackResult(models.TextChoices):
    """The type of feedback that is recieved or sent"""

    APPROVE = "APPROVE", "Approve"
    REJECT = "REJECT", "Reject"


class Feedback(models.Model):
    """
    Represents the evaluation and comments made by a supervisor
    regarding an uploaded evidence.
    """

    comment = models.TextField()
    result_type = models.CharField(max_length=20, choices=FeedbackResult.choices)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    # Relationship with the Uploaded Evidence being reviewed
    uploaded_evidence = models.ForeignKey(
        UploadedEvidence, on_delete=models.CASCADE, related_name="feedbacks"
    )

    # Relationship with the Evaluator (User with supervisor/admin role)
    evaluator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="given_feedbacks",
    )

    def __str__(self):
        return f"Feedback ({self.result_type}) by {self.evaluator.name}"
