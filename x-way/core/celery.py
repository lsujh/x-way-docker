from __future__ import absolute_import
import os

from celery import Celery

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600, periodic_task.s("show_albums"), name="show_albums")


@app.task
def periodic_task(taskname):
    from placeholder.tasks import show_albums

    if taskname == "show_albums":
        show_albums()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
