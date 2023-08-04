from django.core.management.base import BaseCommand
from event_emails.utils import send_event_emails

class Command(BaseCommand):
    help = 'Send event emails'

    def handle(self, *args, **options):
        send_event_emails()
        self.stdout.write(self.style.SUCCESS('Event emails sent and logged successfully.'))
