# Generated by Django 5.2.1 on 2025-06-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemSettingsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='site_title',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='email_service_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
