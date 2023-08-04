from django.contrib import admin
from django.urls import path
from event_emails.views import SendEventEmailsView,EventListAPIView, EmailTemplateListAPIView, EmployeeListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-event-emails/', SendEventEmailsView.as_view(), name='send-event-emails'),
    path('api/events/', EventListAPIView.as_view(), name='event-list'),
    path('api/email-templates/', EmailTemplateListAPIView.as_view(), name='email-template-list'),
    path('api/employees/', EmployeeListAPIView.as_view(), name='employee-list'),
]
