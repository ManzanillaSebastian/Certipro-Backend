import os

from django.core.files.storage import default_storage
from django.db import transaction

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.uploaded_evidences import (
    UploadedEvidence,
    sanitize_filename,
)
from ..serializers.uploaded_evidences import UploadedEvidenceSerializer
from .filter_mixins import QueryParamFilterMixin


class UploadedEvidenceViewSet(
    QueryParamFilterMixin,
    viewsets.ModelViewSet
):

    queryset = UploadedEvidence.objects.all().order_by("-uploaded_at")

    serializer_class = UploadedEvidenceSerializer

    permission_classes = [IsAuthenticated]

    allowed_filters = [
        "id",
        "file_path",
        "description",
        "uploaded_at",
        "task",
        "required_evidence",
    ]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        uploaded_file = serializer.validated_data["file_path"]

        # Original filename
        original_filename = uploaded_file.name

        # Safe filename
        safe_filename = sanitize_filename(original_filename)

        # Get task ID
        task = serializer.validated_data["task"]

        # Create database object WITHOUT saving the file yet
        evidence = UploadedEvidence.objects.create(
            original_filename=original_filename,
            description=serializer.validated_data.get("description"),
            task=task,
            required_evidence=serializer.validated_data["required_evidence"],
        )

        # Now we have the ID
        evidence_id = evidence.id

        # Separate filename and extension
        name, extension = os.path.splitext(safe_filename)

        # Final filename
        final_filename = f"{name}_{evidence_id}{extension}"

        # Final path in Supabase
        final_path = (
            f"evidences/"
            f"required_evidence_{task.id}/"
            f"{final_filename}"
        )

        try:

            # Upload to Supabase
            saved_path = default_storage.save(
                final_path,
                uploaded_file
            )

            # Save path in database
            evidence.file_path = saved_path
            evidence.save(update_fields=["file_path"])

        except Exception:
            # If upload fails, remove the database record
            evidence.delete()
            raise

        response_serializer = self.get_serializer(evidence)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )