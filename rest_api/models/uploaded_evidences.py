import os
import re
import unicodedata

from django.db import models

from .required_evidences import RequiredEvidence
from .tasks import Task


def sanitize_filename(filename):
    """
    Creates a safe filename for Supabase/S3.
    """

    name, extension = os.path.splitext(filename)

    # Remove accents
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")

    # Replace spaces and special characters
    name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)

    # Avoid multiple underscores
    name = re.sub(r"_+", "_", name)

    # Remove underscores at the beginning/end
    name = name.strip("_")

    return f"{name}{extension.lower()}"


class UploadedEvidence(models.Model):

    original_filename = models.CharField(
        max_length=255,
        null=True
    )

    file_path = models.FileField(
        upload_to="evidences/"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        related_name="uploaded_evidences",
        null=True
    )

    required_evidence = models.ForeignKey(
        RequiredEvidence,
        on_delete=models.CASCADE,
        related_name="uploaded_instances"
    )

    def __str__(self):
        return (
            f"File for {self.required_evidence.title} "
            f"- Task: {self.task.title}"
        )