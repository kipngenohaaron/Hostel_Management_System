from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')

    def is_student(self):
        return self.user_type == 'student'

    def is_staff_user(self):
        return self.user_type == 'staff'

    def is_admin_user(self):
        return self.user_type == 'admin'
