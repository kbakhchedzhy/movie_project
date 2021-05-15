import os
from datetime import date, timedelta

from celery import Celery, shared_task
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_api.settings')

app = Celery('Django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@shared_task
def add_new_movie():
    today_date = date.today()
    other_date = date.today() - timedelta(days=1)
    return call_command('MovieForTime', begin=other_date, end=today_date)
