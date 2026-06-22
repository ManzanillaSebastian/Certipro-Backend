"""View for CRUD operations on the users table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.users import User
from ..serializers.users import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage user data.
    Requires JWT authentication for secure access.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
