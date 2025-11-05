from django.contrib import admin
from django.urls import path, include
from hostel.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('hostel/', include('hostel.urls')),
]
