from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','capacity','occupied','vacancies','gender')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student','room','status','applied_at','approved_by')
