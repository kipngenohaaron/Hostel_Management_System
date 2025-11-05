from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Room, Booking
from accounts.models import CustomUser

def home(request):
    return render(request, 'home.html')

@login_required
def room_list(request):
    rooms = Room.objects.all().order_by('room_number')
    return render(request, 'hostel/room_list.html', {'rooms': rooms})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(student=request.user)
    return render(request, 'hostel/my_bookings.html', {'bookings': bookings})

def is_staff_or_admin(user):
    return user.is_authenticated and (user.user_type in ('staff','admin') or user.is_superuser)

@login_required
@user_passes_test(is_staff_or_admin)
def pending_bookings(request):
    bookings = Booking.objects.filter(status='pending')
    return render(request, 'hostel/pending_bookings.html', {'bookings': bookings})

@login_required
def apply_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    # basic check
    if room.vacancies <= 0:
        return redirect('hostel:room_list')
    existing = Booking.objects.filter(student=request.user, status__in=['pending','approved'])
    if existing.exists():
        return redirect('hostel:my_bookings')
    if request.method == 'POST':
        Booking.objects.create(student=request.user, room=room)
        return redirect('hostel:my_bookings')
    return render(request, 'hostel/apply_booking.html', {'room': room})
