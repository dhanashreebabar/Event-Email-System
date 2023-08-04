from django.utils import timezone
from django.core.mail import send_mail
from event_emails.models import Event, EmailTemplate, Employee, EmailLog

def send_event_emails():
    today = timezone.now().date()
    events = Event.objects.filter(event_date=today,processed=False)
    if not events:
        return 'No events scheduled for today.'
            

    for event in events:
        employee = event.employee
        email_template = EmailTemplate.objects.get(event_type=event.event_type)
        email_content = email_template.template_content.format(
            employee_first_name=employee.first_name,
            event_type=event.event_type,
            event_date=event.event_date
        )

        retries = 3
        for attempt in range(retries):
            try:
                send_mail(
                    subject=email_template.template_subject,
                    message=email_content,
                    from_email='your@example.com',  # Replace with your email
                    recipient_list=[employee.email],
                    fail_silently=False
                )
                sent_status = True
                error_message = None
                return "Email sent successfully"
                break  
            except Exception as e:
                sent_status = False
                error_message = str(e)
                # Log the error and retry sending the email if retries remain
                return "Error sending email: {error_message}"
                if attempt < retries - 1:
                    return "Retrying... Attempt {attempt + 1}/{retries}"

            else:
                return "Email sending failed after retries."
                    
        event.processed = True
        event.save()
            
        EmailLog.objects.create(
            event=event,
            email=employee,
            sent_status=sent_status,
            error_message=error_message,
            timestamp=timezone.now() if sent_status else None
        )
