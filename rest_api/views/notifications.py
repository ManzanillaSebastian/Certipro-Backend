"""View for CRUD operations on the notifications table"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.notifications import Notification
from ..serializers.notifications import NotificationSerializer
from .filter_mixins import QueryParamFilterMixin


class NotificationViewSet(QueryParamFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet that lets an authenticated user list and manage their own
    notifications (e.g. evidence rejection alerts).
    """

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    allowed_filters = [
        "id",
        "notification_type",
        "is_read",
        "uploaded_evidence",
        "feedback",
    ]

    def get_queryset(self):
        # A user can only ever see their own notifications.
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by("-created_at")

    @action(detail=True, methods=["post"])
    def mark_read(self, request, pk=None):
        """Marks a single notification as read."""

        notification = self.get_object()
        notification.is_read = True
        notification.save(update_fields=["is_read"])
        return Response(self.get_serializer(notification).data)

    @action(detail=False, methods=["post"])
    def mark_all_read(self, request):
        """Marks every unread notification for the current user as read."""

        updated = self.get_queryset().filter(is_read=False).update(is_read=True)
        return Response({"updated": updated})
