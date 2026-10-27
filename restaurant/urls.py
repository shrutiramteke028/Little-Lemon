from django.urls import include, path
from djoser.views import TokenDestroyView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookingViewSet, MenuItemViewSet

router = DefaultRouter()
router.register('menu', MenuItemViewSet, basename='menu')
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('token/login/', obtain_auth_token, name='token-login'),
    path('token/logout/', TokenDestroyView.as_view(), name='token-logout'),
]
