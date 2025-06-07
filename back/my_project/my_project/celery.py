# myproject/celery.py

import os
from celery import Celery

# Set default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")

app = Celery("my_project")

# Load settings from Django settings file
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all registered Django apps
app.autodiscover_tasks()




from celery.schedules import crontab
from datetime import timedelta

app.conf.beat_schedule = {
    'retry-failed-emails-every-hour': {
        'task': 'systemSettingsApp.tasks.retry_failed_emails',
        'schedule': crontab(minute=0, hour='*'),  # every hour
        # 'schedule': timedelta(seconds=10),  # every 10 seconds
    },
}



# from datetime import timedelta

# app.conf.beat_schedule = {
#     'retry-failed-emails-every-10-seconds': {
#         'task': 'systemSettingsApp.tasks.retry_failed_emails',
#         'schedule': timedelta(seconds=10),  # every 10 seconds
#     },
# }
