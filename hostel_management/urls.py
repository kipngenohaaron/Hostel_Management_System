# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('hostelel.urls')),  # link to your app
# ]
from django.contrib import admin
from django.urls import path, include
from hostel.views import home  # import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),       # homepage
    path('accounts/', include('accounts.urls')),  # login/logout URLs
]
