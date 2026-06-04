# tu_app/models/uploaded_evidences.py
from django.db import models
from .tasks import Task
from .required_evidences import RequiredEvidence

class EvidenceStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending Review'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class UploadedEvidence(models.Model):
    """
    Represents the actual file uploaded by a work group to fulfill 
    a specific required evidence slot for a task.
    """
    file_path = models.FileField(
        upload_to='evidences/', 
        help_text="The actual document uploaded to the server or cloud storage."
    )
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Relationship with the Task
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='uploaded_evidences'
    )
    
    # Relationship with the slot definition (RequiredEvidence)
    required_evidence = models.ForeignKey(
        RequiredEvidence,
        on_delete=models.PROTECT,
        related_name='uploaded_instances'
    )

    def __str__(self):
        return f"File for {self.required_evidence.title} - Task: {self.task.title}"