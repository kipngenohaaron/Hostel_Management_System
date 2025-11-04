from django.contrib import admin
from .models import CustomUser, StudentProfile, StaffProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(StaffProfile)
