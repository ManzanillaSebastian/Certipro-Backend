"""Serializer for CRUD operations on the users table"""

from rest_framework import serializers

from ..models.users import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to expose user fields safely through the API.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "phone_number",
            "is_active",
        ]
        read_only_fields = ["id", "is_active"]
