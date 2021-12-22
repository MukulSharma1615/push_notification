from __future__ import absolute_import, unicode_literals
default_app_config = 'app.apps.appAppConfig'
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.'
#from ..project.celery import app as celery_app
import sys
sys.path.append("..")

__all__ = ('celery_app',)