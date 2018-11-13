from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Patient(models.Model):
    """Patients model which has all the patients information"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=18)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.full_name, self.email)


class Embryo(models.Model):
    """A ForeignKey model to the patient"""
    patient = models.ForeignKey(Patient, related_name="embryos", on_delete=models.CASCADE)
    code_name = models.CharField(max_length=100)
    karyotype = models.CharField(max_length=100)
    down_syndrome = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),

    )
    sex = models.CharField(blank=True, null=True, max_length=1, choices=GENDER_CHOICES)

    def set_sex(self):
        if self.karyotype == "46,XX":
            self.sex = "F"
        elif self.karyotype == "46,XY":
            self.sex = "M"
        else:
            self.sex = ""

    def set_down_syndrome(self):
        if self.karyotype == "47,XY,+21":
            self.down_syndrome = True
            self.sex = "M"
        elif self.karyotype == "47,XX,+21":
            self.down_syndrome = True
            self.sex = "F"
        else:
            self.down_syndrome = False

    def save(self, *args, **kwargs):
        self.set_sex()
        self.set_down_syndrome()
        return super(Embryo, self).save(*args, **kwargs)








