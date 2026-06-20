# rest_api/views/tasks.py
"""View for CRUD operations on the tasks table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.tasks import Task
from ..serializers.tasks import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing operations related to task tracking.
    """
    queryset = Task.objects.all().order_by('end_date')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]