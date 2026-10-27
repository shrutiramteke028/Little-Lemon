from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    inventory = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    contact_email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['reservation_date']

    def __str__(self):
        return f'{self.first_name} - {self.reservation_date:%Y-%m-%d %H:%M}'
