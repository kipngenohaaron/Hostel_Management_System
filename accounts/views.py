from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('dashboard_admin')
            else:
                return redirect('dashboard_student')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required
def dashboard_admin(request):
    return render(request, 'accounts/dashboard_admin.html')


@login_required
def dashboard_student(request):
    return render(request, 'accounts/dashboard_student.html')


def logout_view(request):
    logout(request)
    return redirect('login')
