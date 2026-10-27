LITTLE LEMON CAPSTONE - QUICK README

Run locally:
1. Create and activate a Python virtual environment.
2. pip install -r requirements.txt
3. Copy .env.example to .env and set MySQL credentials.
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Base URL: http://127.0.0.1:8000
Homepage: GET /

Menu API:
GET /api/menu/
POST /api/menu/
GET /api/menu/<id>/
PUT /api/menu/<id>/
PATCH /api/menu/<id>/
DELETE /api/menu/<id>/

Booking API (authenticated users only; each user sees only their own bookings):
GET /api/bookings/
POST /api/bookings/
GET /api/bookings/<id>/
PUT /api/bookings/<id>/
PATCH /api/bookings/<id>/
DELETE /api/bookings/<id>/

Authentication:
POST /api/registration/users/
POST /api/token/login/
POST /api/token/logout/

For protected requests use:
Authorization: Token YOUR_AUTH_TOKEN

Insomnia examples:
Registration JSON: {"username":"ava","email":"ava@example.com","password":"StrongPass123!","re_password":"StrongPass123!"}
Login JSON: {"username":"ava","password":"StrongPass123!"}
Menu create/update JSON: {"title":"Hummus Plate","price":"9.50","inventory":20}
Booking create/update JSON: {"first_name":"Ava","reservation_date":"2030-08-20T19:00:00Z","number_of_guests":2,"contact_email":"ava@example.com","notes":"Window seat"}

Run tests with: python manage.py test
The project is configured for MySQL only; do not replace it with SQLite.
