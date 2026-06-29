"""View for CRUD operations on the users table"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.users import User
from ..serializers.users import UserSerializer


class UserViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet to manage user data.
    Requires JWT authentication for secure access.
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "phone_number",
        "is_active",
    ]
