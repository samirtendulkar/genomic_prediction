from rest_framework import serializers
from .models import Patient, Embryo


class PatientsSerializer(serializers.ModelSerializer):
    """A serializer for the patients model."""

    class Meta:
        model = Patient
        fields = ("id", "user", "first_name", "last_name", "phone", "email", "created_at", "updated_at")


class EmbryoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embryo
        fields = ("id", "patient", "code_name", "karyotype", "sex", "down_syndrome", "created_at", "updated_at")
        extra_kwargs = {"sex": {"read_only": True},
                        "down_syndrome": {"read_only": True}
                        }





