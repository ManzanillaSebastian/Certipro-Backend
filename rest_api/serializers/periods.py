"""Serializer for CRUD operations on periods table"""

from rest_framework import serializers

from ..models.periods import Period


class PeriodSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Period data to and from JSON.
    """

    class Meta:
        model = Period
        fields = [
            "id",
            "name",
            "reason",
            "allow_editing",
            "start_date",
            "end_date",
            "certification_model",
        ]
