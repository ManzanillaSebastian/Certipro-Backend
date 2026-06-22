"""View for CRUD operations on the feedbacks table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filter_mixins import QueryParamFilterMixin
from ..models.feedbacks import Feedback
from ..serializers.feedbacks import FeedbackSerializer

class FeedbackViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for logging and auditing supervisor reviews.
    """
    queryset = Feedback.objects.all().order_by('-reviewed_at')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = ['id', 'comment', 'result_type', 'reviewed_at', 'uploaded_evidence', 'evaluator']