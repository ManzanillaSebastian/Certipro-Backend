"""Signal handlers for the rest_api app."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.feedbacks import Feedback, FeedbackResult
from .models.notifications import Notification, NotificationType


@receiver(post_save, sender=Feedback)
def notify_members_on_evidence_rejected(sender, instance, created, **kwargs):
    """
    Whenever a supervisor leaves a Feedback with result_type=REJECT on an
    uploaded evidence, notify every member of the work group responsible
    for the related task so they know the evidence needs attention.
    """

    if not created or instance.result_type != FeedbackResult.REJECT:
        return

    evidence = instance.uploaded_evidence
    task = evidence.task
    group = task.group_responsible

    required_evidence_title = evidence.required_evidence.title
    message = (
        f'Tu evidencia "{required_evidence_title}" para la tarea '
        f'"{task.title}" fue rechazada. Motivo: {instance.comment}'
    )

    notifications = [
        Notification(
            recipient=member,
            notification_type=NotificationType.EVIDENCE_REJECTED,
            message=message,
            uploaded_evidence=evidence,
            feedback=instance,
        )
        for member in group.members.all()
    ]

    if notifications:
        Notification.objects.bulk_create(notifications)
