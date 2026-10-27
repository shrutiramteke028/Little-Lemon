from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from .models import Booking, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Title cannot be blank.')
        return value.strip()


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'first_name', 'reservation_date', 'number_of_guests', 'contact_email', 'notes', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_reservation_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('Reservation date must be in the future.')
        return value

    def validate_number_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError('Number of guests must be at least 1.')
        return value

    def create(self, validated_data):
        return Booking.objects.create(user=self.context['request'].user, **validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    re_password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 're_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({'re_password': 'Passwords do not match.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('re_password')
        return get_user_model().objects.create_user(**validated_data)
