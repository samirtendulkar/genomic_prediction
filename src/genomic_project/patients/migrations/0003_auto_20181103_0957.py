# Generated by Django 2.1.2 on 2018-11-03 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_embryo_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embryo',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patients'),
        ),
    ]
