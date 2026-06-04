from django.db import models

class Requirement(models.Model):
    """
    Global catalog of certification requirements. 
    Acts as a reusable template independent of any specific certification model.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class RequirementVersion(models.Model):
    """
    Handles versioning for global requirements.
    """
    requirement = models.ForeignKey(
        Requirement, 
        on_delete=models.CASCADE, 
        related_name='versions'
    )

    version_number = models.CharField(max_length=20, help_text="e.g., v1.0, 2026-A")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('requirement', 'version_number')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.requirement.title} ({self.version_number})"