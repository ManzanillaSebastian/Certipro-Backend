"""View for CRUD operations on the criteria table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.criteria import Criterion
from ..serializers.criteria import CriterionSerializer

class CriterionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and managing evaluation criteria and sub-criteria.
    """
    serializer_class = CriterionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Criterion.objects.all().order_by('code')

        allowed_filters = {
            'certification_model',
            'parent',
            'priority',
            'code',
            'title',
        }

        filter_params = {
            key: value
            for key, value in self.request.query_params.items()
            if key in allowed_filters and value != ''
        }

        if filter_params:
            queryset = queryset.filter(**filter_params)

        return queryset