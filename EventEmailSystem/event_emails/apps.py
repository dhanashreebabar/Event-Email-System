from django.apps import AppConfig


class EventEmailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_emails'
    
    def ready(self):
        import event_emails.signals