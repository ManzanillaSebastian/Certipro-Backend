from django.db import models
from .requirements import RequirementVersion

class RequiredEvidence(models.Model):
    """
    Defines the specific files or documents that must be submitted 
    to satisfy a particular requirement version.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_type = models.CharField(
        max_length=100, 
        help_text="Expected file extension or MIME type, e.g., .pdf, .png, .docx"
    )
    
    # Linked to the reusable requirement version catalog
    requirement_version = models.ForeignKey(
        RequirementVersion,
        on_delete=models.CASCADE,
        related_name='required_evidences'
    )

    def __str__(self):
        return f"{self.title} ({self.file_type})"