from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


from . import serializers
from .models import Patient, Embryo


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns a auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class PatientsApiView(viewsets.ModelViewSet):
    """Handles Creating, reading and updating Patients"""

    serializer_class = serializers.PatientsSerializer
    queryset = Patient.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ("first_name", "last_name", "phone", "email",)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmbroApiView(viewsets.ModelViewSet):
    """Handles Creating, reading and updating Patients"""

    serializer_class = serializers.EmbryoSerializer
    queryset = Embryo.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ("code_name", "karyotype", "sex", "down_syndrome",)

    def perform_create(self, serializer):
        serializer.save(patient__id=self.kwargs['pk'])








