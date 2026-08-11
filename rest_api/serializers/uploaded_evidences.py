from rest_framework import serializers

from ..models.uploaded_evidences import UploadedEvidence


class UploadedEvidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedEvidence

        fields = [
            "id",
            "original_filename",
            "file_path",
            "description",
            "uploaded_at",
            "task",
            "required_evidence",
        ]

        read_only_fields = [
            "id",
            "original_filename",
            "uploaded_at",
        ]