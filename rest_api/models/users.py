from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrator'
    SUPERVISOR = 'SUPERVISOR', 'Supervisor'
    MEMBER = 'MEMBER', 'Team Member'

class User(AbstractUser):
    """
    Custom User model to handle authentication and specific system roles
    within the certification platform.
    """
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.MEMBER
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"