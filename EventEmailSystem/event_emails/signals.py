from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from .models import Employee, Event, EmailTemplate

@receiver(post_save, sender=Employee)
def update_email_template(sender, instance, **kwargs):
    today = datetime.today().date()
    event_type_birthdate = "Birthday"
    event_type_anniversary = "Work Anniversary"

    if instance.date_of_birth.month == today.month and instance.date_of_birth.day == today.day:
        email_template, _ = EmailTemplate.objects.get_or_create(event_type=event_type_birthdate)
        email_template.template_subject = f"Happy Birthday, {instance.first_name}!"
        email_template.template_content = f"Dear {instance.first_name},\n\nWishing you a fantastic birthday today!"
        email_template.save()

        Event.objects.get_or_create(
            employee=instance,
            event_type=event_type_birthdate,
            event_date=today
        )


    if instance.hire_date.month == today.month and instance.hire_date.day == today.day:
        email_template, _ = EmailTemplate.objects.get_or_create(event_type=event_type_anniversary)
        email_template.template_subject = f"Congratulations on your Work Anniversary, {instance.first_name}!"
        email_template.template_content = f"Dear {instance.first_name},\n\nThank you for your dedication and hard work."
        email_template.save()

        Event.objects.get_or_create(
            employee=instance,
            event_type=event_type_anniversary,
            event_date=today,
           
        )
