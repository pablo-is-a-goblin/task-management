import os
from celery import Celery
from . import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object(settings)
app.conf.result_backend = settings.BROKER_URL
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
