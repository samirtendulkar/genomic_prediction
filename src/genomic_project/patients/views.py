from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.template.loader import get_template
from django.core.mail import EmailMessage


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
        patient = serializer.save()
        try:
            patient_create_email(patient_id=patient.id)
            print('An email has been sent to the customer.')
        except IOError as e:
            return e

    def perform_update(self, serializer):
        patient = serializer.save()
        try:
            patient_update_email(patient_id=patient.id)
            print('An email has been sent to the customer.')
        except IOError as e:
            return e


class EmbroApiView(viewsets.ModelViewSet):
    """Handles Creating, reading and updating Patients"""

    serializer_class = serializers.EmbryoSerializer
    queryset = Embryo.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ("code_name", "karyotype", "sex", "down_syndrome",)

    def perform_create(self, serializer):
        serializer.save(pk=self.kwargs.get("pk"))
        embryo = serializer.save()
        try:
            embryo_create_email(patient_id=embryo.patient.id)
            print('An email has been sent to the customer.')
        except IOError as e:
            return e

    def perform_update(self, serializer):
        serializer.save(pk=self.kwargs.get("pk"))
        embryo = serializer.save()
        try:
            embryo_update_email(patient_id=embryo.patient.id)
            print('An email has been sent to the customer.')
        except IOError as e:
            return e


def patient_create_email(patient_id):
    patient = Patient.objects.get(id=patient_id)
    embryos = Embryo.objects.filter(patient=patient)
    try:
        '''Sending the Update to the patient'''
        subject = "Gemonic Prediction added you to the system #{}".format(patient_id)
        to = ['{}'.format(patient.email)]
        from_email = "no_reply@genomicprediction.com/"
        patient_information = {
            'patient': patient,
            'embryos': embryos
        }
        message = get_template('patients/email.html').render(patient_information)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    except IOError as e:
        return e


def patient_update_email(patient_id):
    patient = Patient.objects.get(id=patient_id)
    embryos = Embryo.objects.filter(patient=patient)
    try:
        '''Sending the Update to the patient'''
        subject = "Gemonic Prediction updated your details #{}".format(patient_id)
        to = ['{}'.format(patient.email)]
        from_email = "no_reply@genomicprediction.com/"
        patient_information = {
            'patient': patient,
            'embryos': embryos
        }
        message = get_template('patients/email.html').render(patient_information)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    except IOError as e:
        return e


def embryo_create_email(patient_id):
    patient = Patient.objects.get(id=patient_id)
    embryos = Embryo.objects.filter(patient=patient)
    try:
        '''Sending the Create to the Embryo'''
        subject = "Gemonic Prediction created a new Embryo for you #{}".format(patient_id)
        to = ['{}'.format(patient.email)]
        from_email = "no_reply@genomicprediction.com/"
        patient_information = {
            'patient': patient,
            'embryos': embryos
        }
        message = get_template('patients/email.html').render(patient_information)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    except IOError as e:
        return e


def embryo_update_email(patient_id):
    patient = Patient.objects.get(id=patient_id)
    embryos = Embryo.objects.filter(patient=patient)
    try:
        '''Sending the Update to the Embryo'''
        subject = "Gemonic Prediction updated your Embryo #{}".format(patient_id)
        to = ['{}'.format(patient.email)]
        from_email = "no_reply@genomicprediction.com/"
        patient_information = {
            'patient': patient,
            'embryos': embryos
        }
        message = get_template('patients/email.html').render(patient_information)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    except IOError as e:
        return e





