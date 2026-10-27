from django.contrib import admin
from django.urls import include, path
from restaurant.views import RegistrationView, home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/registration/', RegistrationView.as_view(), name='registration'),
    path('api/', include('restaurant.urls')),
    path('api/registration/', include('djoser.urls')), 
    path('api/registration/', include('djoser.urls.authtoken')),
]
