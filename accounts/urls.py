from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/staff/', views.dashboard_staff, name='dashboard_staff'),
    path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
]
