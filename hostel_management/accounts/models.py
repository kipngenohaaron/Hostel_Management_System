# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# # Define role choices
# ROLE_CHOICES = (
#     ('student', 'Student'),
#     ('staff', 'Staff'),
#     ('admin', 'Admin'),
# )

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    reg_no = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10, blank=True, null=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    staff_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
