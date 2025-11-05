# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import get_user_model

# User = get_user_model()

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.user_type == 'ADMIN':
#                 return redirect('admin_dashboard')
#             elif user.user_type == 'STUDENT':
#                 return redirect('student_dashboard')
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'accounts/login.html')


# @login_required
# def admin_dashboard(request):
#     return render(request, 'accounts/dashboard_admin.html')


# @login_required
# def student_dashboard(request):
#     return render(request, 'accounts/dashboard_student.html')


# def logout_view(request):
#     logout(request)
#     return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_admin:
                return redirect('dashboard_admin')
            elif user.is_student:
                return redirect('dashboard_student')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard_admin(request):
    return render(request, 'accounts/dashboard_admin.html')

@login_required
def dashboard_student(request):
    return render(request, 'accounts/dashboard_student.html')

def logout_view(request):
    logout(request)
    return redirect('login')
