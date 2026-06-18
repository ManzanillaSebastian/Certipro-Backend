"""View for CRUD operations on the departments table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.departments import Department
from ..serializers.departments import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing branch departments.
    """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]