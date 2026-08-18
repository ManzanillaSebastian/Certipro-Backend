from django.db import models

from .criteria import Criterion
from .requirements import RequirementVersion
from .work_groups import WorkGroup


class Task(models.Model):
    """
    Represents an assignment where a work group must fulfill a specific
    requirement version within a criterion and a time window.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # Relationship with Criterion
    criterion = models.ForeignKey(
        Criterion, on_delete=models.CASCADE, related_name="tasks"
    )

    # Relationship with the global catalog (RequirementVersion)
    # If a requirement version is deleted/protected, we preserve or block here.
    requirement_version = models.ForeignKey(
        RequirementVersion, on_delete=models.CASCADE, related_name="tasks"
    )

    # Relationship with the responsible team
    group_responsible = models.ForeignKey(
        WorkGroup, on_delete=models.PROTECT, related_name="tasks"
    )

    def __str__(self):
        return f"{self.title} -> {self.group_responsible.name}"
