from django.db import models
from django.contrib.auth.models import User


class Patients(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=18)
    email = models.EmailField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Embryo(models.Model):
    code_name = models.CharField(max_length=100)
    karyotype = models.CharField(max_length=100)
    down_syndrome = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),

    )
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)

