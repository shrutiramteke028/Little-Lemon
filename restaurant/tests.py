from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .models import Booking, MenuItem


class LittleLemonAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='owner', password='StrongPass123!', email='owner@example.com')
        self.other = get_user_model().objects.create_user(username='other', password='StrongPass123!')
        self.menu = MenuItem.objects.create(title='Greek Salad', price='12.50', inventory=10)

    def auth(self, user=None):
        self.client.force_authenticate(user=user or self.user)

    def test_homepage_returns_200(self):
        self.assertEqual(self.client.get('/').status_code, status.HTTP_200_OK)

    def test_menu_list_and_detail(self):
        self.assertEqual(self.client.get('/api/menu/').status_code, status.HTTP_200_OK)
        response = self.client.get(f'/api/menu/{self.menu.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Greek Salad')

    def test_authorized_menu_create_update_delete(self):
        self.auth()
        created = self.client.post('/api/menu/', {'title': 'Pasta', 'price': '16.00', 'inventory': 4}, format='json')
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        item_id = created.data['id']
        self.assertEqual(self.client.patch(f'/api/menu/{item_id}/', {'price': '17.00'}, format='json').status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.delete(f'/api/menu/{item_id}/').status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_menu_data_rejected(self):
        self.auth()
        self.assertEqual(self.client.post('/api/menu/', {'title': '', 'price': '-2', 'inventory': 1}, format='json').status_code, status.HTTP_400_BAD_REQUEST)

    def test_booking_creation_requires_authentication(self):
        data = {'first_name': 'Ava', 'reservation_date': (timezone.now() + timedelta(days=2)).isoformat(), 'number_of_guests': 2}
        self.assertEqual(self.client.post('/api/bookings/', data, format='json').status_code, status.HTTP_401_UNAUTHORIZED)
        self.auth()
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.pk)

    def test_users_only_see_and_modify_own_bookings(self):
        booking = Booking.objects.create(user=self.other, first_name='Other', reservation_date=timezone.now() + timedelta(days=1), number_of_guests=2)
        self.auth()
        self.assertEqual(self.client.get('/api/bookings/').data, [])
        self.assertEqual(self.client.get(f'/api/bookings/{booking.pk}/').status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(self.client.delete(f'/api/bookings/{booking.pk}/').status_code, status.HTTP_404_NOT_FOUND)

    def test_registration_and_token_authentication(self):
        response = self.client.post('/api/registration/users/', {'username': 'newuser', 'password': 'AnotherStrong123!', 're_password': 'AnotherStrong123!', 'email': 'new@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        login = self.client.post('/api/token/login/', {'username': 'newuser', 'password': 'AnotherStrong123!'}, format='json')
        self.assertEqual(login.status_code, status.HTTP_200_OK)
        self.assertTrue(Token.objects.filter(key=login.data['auth_token']).exists())

    def test_missing_records_return_404(self):
        self.assertEqual(self.client.get('/api/menu/99999/').status_code, status.HTTP_404_NOT_FOUND)
