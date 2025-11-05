# Hostel Management System (Django)

This is a starter Django project for a Hostel Management System.
It includes:
- Custom user model (accounts.CustomUser) with user_type (admin/staff/student)
- Hostel app with Room and Booking models
- Basic templates and pages for login and role dashboards

## Quick start
1. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Create a superuser:
   python manage.py createsuperuser

5. Run the server:
   python manage.py runserver

Visit http://127.0.0.1:8000/
