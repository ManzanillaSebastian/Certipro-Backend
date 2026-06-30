from django.db import models

from .certification_models import CertificationModel


class Period(models.Model):
    """
    Defines a specific time frame associated with a certification model,
    controlling whether edits are allowed during this block.
    """

    name = models.CharField(max_length=255)
    reason = models.TextField(blank=True, null=True)
    allow_editing = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # Relationship with CertificationModel
    certification_model = models.ForeignKey(
        CertificationModel, on_delete=models.CASCADE, related_name="periods"
    )

    def __str__(self):
        return f"{self.name} ({self.certification_model.title})"
