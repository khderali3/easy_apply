# Generated by Django 5.2.1 on 2025-06-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersAuthApp', '0007_rename_created_data_useraccount_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='preferred_language',
            field=models.CharField(choices=[('en', 'English'), ('ar', 'Arabic')], default='en', max_length=2),
        ),
    ]
