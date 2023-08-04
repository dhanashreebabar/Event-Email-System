from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_event_emails  
from .models import Event, EmailTemplate, Employee
from .serializers import EventSerializer, EmailTemplateSerializer, EmployeeSerializer
from rest_framework import generics

class SendEventEmailsView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            send_event_emails()  
            return Response({'message': 'Event emails sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EmailTemplateListAPIView(generics.ListAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer