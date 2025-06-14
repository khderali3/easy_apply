# Generated by Django 5.2.1 on 2025-06-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemSettingsApp', '0011_mainconfiguration_is_captcha_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueuedEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('is_html', models.BooleanField(default=False)),
                ('status', models.CharField(default='queued', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('error', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
