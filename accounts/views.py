from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if getattr(user, 'user_type', '') == 'admin':
                return redirect('accounts:dashboard_admin')
            elif getattr(user, 'user_type', '') == 'staff':
                return redirect('accounts:dashboard_staff')
            else:
                return redirect('accounts:dashboard_student')
        else:
            error_message = 'Invalid credentials'
    return render(request, 'accounts/login.html', {'error_message': error_message})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_admin(request):
    return render(request, 'accounts/dashboard_admin.html')

@login_required
def dashboard_staff(request):
    return render(request, 'accounts/dashboard_staff.html')

@login_required
def dashboard_student(request):
    return render(request, 'accounts/dashboard_student.html')
