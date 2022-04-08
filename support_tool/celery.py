import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_tool.settings')
app = Celery('support_tool')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()