"""Everything related to the user"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.TextChoices):
    """User role text choices class"""

    ADMIN = "ADMINISTRADOR"
    SUPERVISOR = "SUPERVISOR"
    MEMBER = "MIEMBRO DE EQUIPO"


class User(AbstractUser):
    """
    Custom User model to handle authentication and specific system roles
    within the certification platform.
    """

    email = models.EmailField(unique=True, max_length=100)
    USERNAME_FIELD = "email"

    role = models.CharField(
        max_length=20, choices=UserRole.choices, default=UserRole.MEMBER
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    REQUIRED_FIELDS = ["username", "password", "role"]

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"
