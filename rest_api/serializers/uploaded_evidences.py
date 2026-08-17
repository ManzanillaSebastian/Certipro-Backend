import os
from rest_framework import serializers
from ..models.uploaded_evidences import UploadedEvidence

class UploadedEvidenceSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedEvidence
        fields = [
            "id",
            "original_filename",
            "file_path",
            "file_url", # <- Devolverá la URL pública directa
            "description",
            "uploaded_at",
            "task",
            "required_evidence",
        ]
        read_only_fields = ["id", "original_filename", "uploaded_at"]

    def get_file_url(self, obj):
        if obj.file_path:
            # Obtenemos el ID del proyecto de tus variables de entorno o settings
            project_id = os.getenv("SUPABASE_PROJECT_ID")
            bucket_name = "certipro-storage"
            
            # obj.file_path ya contiene algo como "evidences/required_evidence_2/archivo.pdf"
            clean_path = str(obj.file_path)
            
            # Construimos la URL pública exacta de Supabase
            return f"https://{project_id}.supabase.co/storage/v1/object/public/{bucket_name}/{clean_path}"
        return None