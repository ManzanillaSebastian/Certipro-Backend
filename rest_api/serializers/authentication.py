"""Serializer for authentication"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizes the JWT response to include user metadata such as full name and role.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 💡 Campos adicionales inyectados dentro del JWT encriptado:
        # Esto le sirve al frontend para leer el rol sin volver a consultar el backend.
        token["username"] = user.username
        token["role"] = user.role
        token["full_name"] = user.get_full_name()

        return token

    def validate(self, attrs):
        # Ejecuta la validación por defecto de usuario y contraseña
        data = super().validate(attrs)

        # También añadimos los campos en la respuesta JSON plana del login
        data["user"] = {
            "username": self.user.username,
            "email": self.user.email,
            "full_name": self.user.get_full_name(),
            "role": self.user.role,
        }
        return data
