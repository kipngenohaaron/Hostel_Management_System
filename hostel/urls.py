from django.urls import path
from . import views

app_name = 'hostel'

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/apply/<int:room_id>/', views.apply_booking, name='apply_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('pending/', views.pending_bookings, name='pending_bookings'),
]
