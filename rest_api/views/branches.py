"""View for acruda operations on the branches table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.branches import Branch
from ..serializers.branches import BranchSerializer

class BranchViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing organizational branches.
    """
    queryset = Branch.objects.all().order_by('name')
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ['id', 'name', 'location', 'supervisor']