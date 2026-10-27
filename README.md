# Little Lemon Django REST Framework Capstone

Little Lemon is a Django 4.2 restaurant application with a template-rendered homepage, MySQL persistence, Django REST Framework APIs, token authentication, Djoser registration, and a staff admin interface.

## Features

- Responsive homepage at `/` rendered by a Django template.
- Public menu reads; authenticated menu create, update, and delete operations.
- Authenticated booking CRUD restricted to the owning user.
- Djoser registration at `/api/registration/users/` and token login/logout.
- Django admin at `/admin/`.
- Automated `TestCase`/`APIClient` coverage.

## Prerequisites and installation

Python 3.10+ and MySQL 8+ are recommended. Create a database and user:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'change-this-password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon_user'@'localhost';
FLUSH PRIVILEGES;
```

Then:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Windows: copy .env.example .env
```

Edit `.env` with your own secret key and MySQL credentials. Never commit `.env`.

```bash
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. This project intentionally configures MySQL and does not silently substitute SQLite. If MySQL is unavailable, setup and test commands requiring database access will remain unverified until MySQL is running.

## API endpoints

- `GET /api/menu/`, `POST /api/menu/`
- `GET|PUT|PATCH|DELETE /api/menu/<id>/`
- `GET /api/bookings/`, `POST /api/bookings/`
- `GET|PUT|PATCH|DELETE /api/bookings/<id>/`
- `POST /api/registration/users/`
- `POST /api/token/login/`, `POST /api/token/logout/`

Menu GET is public. Menu writes and all booking operations require authentication. Booking querysets contain only the authenticated user's records. Use `Authorization: Token YOUR_AUTH_TOKEN` in Insomnia or the browsable API.

Example request bodies:

```json
// registration
{"username":"ava","email":"ava@example.com","password":"StrongPass123!","re_password":"StrongPass123!"}
// token login
{"username":"ava","password":"StrongPass123!"}
// menu creation/update
{"title":"Hummus Plate","price":"9.50","inventory":20}
// booking creation/update
{"first_name":"Ava","reservation_date":"2030-08-20T19:00:00Z","number_of_guests":2,"contact_email":"ava@example.com","notes":"Window seat"}
```

Expected responses include `200` for successful reads/updates, `201` for creates, `204` for deletes, `400` for invalid data, `401` for unauthenticated protected operations, and `404` for missing or inaccessible records.

## Tests

With MySQL configured and available:

```bash
python manage.py test
```

## GitHub upload

Create an empty repository on GitHub, then from this folder:

```bash
git init
git add .
git commit -m "Build Little Lemon Django REST API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the placeholder remote with the repository URL you actually create. No repository is claimed to have been uploaded by this project.
