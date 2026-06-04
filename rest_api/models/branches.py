from django.db import models
from django.conf import settings

class Branch(models.Model):
    """
    Represents a physical or logical branch of the organization.
    """
    name = models.CharField(max_length=255)
    location = models.TextField(blank=True, null=True)
    
    # Foreign Key pointing to the custom User model
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='supervised_branches',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name