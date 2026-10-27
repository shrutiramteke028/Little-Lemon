from django.contrib import admin
from .models import Booking, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'reservation_date', 'number_of_guests', 'user')
    list_filter = ('reservation_date',)
    search_fields = ('first_name', 'contact_email')
