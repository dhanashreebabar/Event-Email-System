from django.test import TestCase
from datetime import date, timedelta
from event_emails.models import Employee, Event, EmailLog
from event_emails.utils import send_event_emails

class EventEmailTestCase(TestCase):
    def setUp(self):
        self.employee_with_birthday = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            date_of_birth=date.today(),
            hire_date=date.today() - timedelta(days=365)
        )

        self.employee_with_anniversary = Employee.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            date_of_birth=date.today() - timedelta(days=365),
            hire_date=date.today()
        )

        self.birthday_event = Event.objects.create(
            employee=self.employee_with_birthday,
            event_type="Birthday",
            event_date=date.today()
        )

        self.anniversary_event = Event.objects.create(
            employee=self.employee_with_anniversary,
            event_type="Work Anniversary",
            event_date=date.today()
        )

    def test_send_birthday_email(self):
        send_event_emails()

        # Verify that the email logs were created
        self.assertEqual(EmailLog.objects.filter(event=self.birthday_event).count(), 1)
        print(EmailLog.objects.filter(event=self.birthday_event))

    def test_send_anniversary_email(self):
        send_event_emails()

        # Verify that the email logs were created
        self.assertEqual(EmailLog.objects.filter(event=self.anniversary_event).count(), 1)

    def test_no_events(self):
        # Delete the events to simulate no scheduled events
        Event.objects.all().delete()

        send_event_emails()

        # Verify that no email logs were created
        self.assertEqual(EmailLog.objects.all().count(), 0)
