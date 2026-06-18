"""View for CRUD operations on the feedbacks table"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.feedbacks import Feedback
from ..serializers.feedbacks import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    """
    ViewSet for logging and auditing supervisor reviews.
    """
    queryset = Feedback.objects.all().order_by('-reviewed_at')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]