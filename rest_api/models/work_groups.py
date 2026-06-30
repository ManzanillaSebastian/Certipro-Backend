"""Model for the Work Groups table"""

from django.conf import settings
from django.db import models

from .departments import Department


class WorkGroup(models.Model):
    """
    Represents a work group within a specific department.
    Manages both its supervisor and its assigned members.
    """

    name = models.CharField(max_length=255)

    # Relationship with Department
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="work_groups"
    )

    # Group Supervisor (User)
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="supervised_groups",
        blank=True,
        null=True,
    )

    # Many-to-Many relationship for group members
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="work_groups_joined", blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.department.name})"
