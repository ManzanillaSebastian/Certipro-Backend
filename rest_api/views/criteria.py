"""View for CRUD operations on the criteria table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.criteria import Criterion
from ..serializers.criteria import CriterionSerializer

class CriterionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing evaluation criteria and sub-criteria.
    """
    queryset = Criterion.objects.all().order_by('code')
    serializer_class = CriterionSerializer
    permission_classes = [IsAuthenticated]