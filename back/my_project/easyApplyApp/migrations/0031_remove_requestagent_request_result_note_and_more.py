# Generated by Django 5.2.1 on 2025-06-15 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyApplyApp', '0030_alter_requestservice_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestagent',
            name='request_result_note',
        ),
        migrations.RemoveField(
            model_name='requestservice',
            name='request_result_note',
        ),
    ]
