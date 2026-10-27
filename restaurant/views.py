from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, MenuItem
from .permissions import IsBookingOwner, MenuItemPermission
from .serializers import BookingSerializer, MenuItemSerializer, RegistrationSerializer


def home(request):
    return render(request, 'restaurant/index.html', {'menu_items': MenuItem.objects.all()[:6]})


class RegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {'id': user.pk, 'username': user.username, 'email': user.email},
            status=status.HTTP_201_CREATED,
        )


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermission]


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingOwner]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
