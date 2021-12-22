from django.apps import AppConfig

class appAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    def ready(self):
        import app.signal_with_celery
