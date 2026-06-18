from django.db import models
from django.conf import settings
from .branches import Branch

class Department(models.Model):
    """
    Represents an internal department within a specific branch.
    """
    name = models.CharField(max_length=255)
    
    # Relationship with Branch
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    
    # Relationship with Supervisor (User)
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='supervised_departments',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.branch.name}"