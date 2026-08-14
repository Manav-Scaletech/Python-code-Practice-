from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SIGNAL'

    def ready(self):
        # This registration connect signals to receivers
        pass    
