from django.contrib import admin
from .models import Patient, Embryo


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'created_at', 'updated_at')


class EmbryoAdmin(admin.ModelAdmin):
    list_display = ('patient', 'code_name', 'karyotype', 'down_syndrome', 'sex', 'created_at', 'updated_at')


admin.site.register(Patient, PatientAdmin)
admin.site.register(Embryo, EmbryoAdmin)

