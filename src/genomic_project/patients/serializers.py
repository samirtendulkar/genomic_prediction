from rest_framework import serializers
from .models import Patient, Embryo


class PatientsSerializer(serializers.ModelSerializer):
    """A serializer for the patients model."""

    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "phone", "email")

    def create(self, validated_data):
        """Create and return a new patient"""

        patient = Patient(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            email=validated_data["email"]
        )
        patient.save()
        return patient


class EmbryoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embryo
        fields = ("id", "patient", "code_name", "karyotype", "down_syndrome", "sex")

        def create(self, validated_data):
            """Create and return a new embryo"""

            embryo = Embryo(
                code_name=validated_data["code_name"],
                karyotype=validated_data["karyotype"],
                down_syndrome=validated_data["down_syndrome"],
                sex=validated_data["sex"]
            )
            embryo.save()
            return embryo



