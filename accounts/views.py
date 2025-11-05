from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Admin dashboard
                return redirect('dashboard_admin')
            else:  # Normal user/student dashboard
                return redirect('dashboard_student')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Admin Dashboard
@login_required
def dashboard_admin(request):
    context = {}
    return render(request, 'accounts/dashboard_admin.html', context)


# Student Dashboard
@login_required
def dashboard_student(request):
    context = {}
    return render(request, 'accounts/dashboard_student.html', context)
