# Generated by Django 2.1.2 on 2018-11-03 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20181103_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]