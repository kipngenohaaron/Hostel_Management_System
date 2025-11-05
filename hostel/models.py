from django.db import models
from django.conf import settings

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField(default=1)
    occupied = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=(('male','Male'),('female','Female'),('mixed','Mixed')), default='mixed')
    description = models.TextField(blank=True)

    @property
    def vacancies(self):
        return max(self.capacity - self.occupied, 0)

    def __str__(self):
        return f"Room {self.room_number} ({self.occupied}/{self.capacity})"

class Booking(models.Model):
    STATUS_CHOICES = (('pending','Pending'),('approved','Approved'),('rejected','Rejected'))
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='approvals')

    def __str__(self):
        return f"{self.student.username} -> {self.room.room_number} ({self.status})"
