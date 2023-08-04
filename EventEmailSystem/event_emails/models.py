from django.db import models
from django.utils import timezone

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    date_of_birth = models.DateField(default=timezone.now)

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()
    processed = models.BooleanField(default=False)  


class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50, unique=True)
    template_subject = models.CharField(max_length=100)
    template_content = models.TextField()

class EmailLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sent_status = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
