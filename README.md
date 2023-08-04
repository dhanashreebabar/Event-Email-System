# Event-Email-System

Overview

The event email system is designed to automatically send emails on special occasions such as birthdays, and work anniversaries. The system retrieves the event details from its table containing employee ID, event types, and dates. Templates for each event type are also stored in the Django database. The system sends emails to the people on that date using the corresponding email template.

Features
Automatic retrieval of event data from the database
Personalized email generation based on event type
Retry mechanism for failed email sending
Logging of email sending status and errors
Scheduled execution to ensure timely emails

Installation
Clone the repository:

     git clone https://github.com/your-username/event-email-system.git


Navigate to the project directory:


    cd EventEmailSystem
    
Create and activate a virtual environment:


    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

    
Install the project dependencies:

    pip install -r requirements.txt
    
Usage
Run migrations to set up the database:

        python manage.py migrate
    
Populate the database with event data and templates.

Run the automated email sending process:

    python manage.py send_event_emails
Run server:

    python manage.py runserver
 and test api end points  http://127.0.0.1:8000/send-event-emails/ ,   http://127.0.0.1:8000/api/employees/ ,   http://127.0.0.1:8000/api/events/ , http://127.0.0.1:8000/api/email-templates/
 
Configuration:

Configure your email settings in the settings.py file.
Customize email templates in the database according to event types.

Tests:
Run tests to ensure the functionality of the system:

    python manage.py test






