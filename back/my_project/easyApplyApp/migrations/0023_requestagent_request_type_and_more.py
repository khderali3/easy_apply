# Generated by Django 5.2.1 on 2025-06-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyApplyApp', '0022_cardlabelcheckrequest_request_form_sub_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestagent',
            name='request_type',
            field=models.CharField(default='agent'),
        ),
        migrations.AddField(
            model_name='requestservice',
            name='request_type',
            field=models.CharField(default='service'),
        ),
    ]
