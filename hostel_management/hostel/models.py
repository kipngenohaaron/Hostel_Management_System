# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Room(models.Model):
#     ROOM_TYPE_CHOICES = (
#         ('single', 'Single'),
#         ('double', 'Double'),
#         ('shared', 'Shared'),
#     )

#     room_number = models.CharField(max_length=10, unique=True)
#     room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
#     capacity = models.PositiveIntegerField(default=1)
#     occupied = models.BooleanField(default=False)
#     price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Room {self.room_number} ({self.room_type})"


# class Booking(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#     )

#     student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     date_booked = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_bookings')

#     def __str__(self):
#         return f"{self.student.username} - {self.room.room_number} ({self.status})"
from django.db import models
from accounts.models import StudentProfile

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    warden = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hostel.name} - {self.room_number}"


class Allocation(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    date_allocated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} → {self.room.room_number}"
