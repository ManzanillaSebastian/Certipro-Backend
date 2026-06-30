"""Model for the criteria table"""

from django.db import models

from .certification_models import CertificationModel


class CriterionPriority(models.TextChoices):
    HIGH = "Alta"
    MEDIUM = "Media"
    LOW = "Baja"


class Criterion(models.Model):
    """
    Represents a evaluation criterion or sub-criterion within a certification model.
    Supports a tree-like hierarchical structure via self-reference.
    """

    priority = models.CharField(
        max_length=20, choices=CriterionPriority.choices, default=CriterionPriority.LOW
    )

    code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Relationship with the Certification Model
    certification_model = models.ForeignKey(
        CertificationModel, on_delete=models.CASCADE, related_name="criteria"
    )

    # Self-reference for sub-criteria (Recursive relationship)
    # Allows a criterion to have a parent criterion.
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcriteria",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Criteria"
        unique_together = ("certification_model", "code")

    def __str__(self):
        return f"{self.code} - {self.title}"
