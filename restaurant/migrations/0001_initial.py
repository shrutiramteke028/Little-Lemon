from django.conf import settings
from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='MenuItem', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=100, unique=True)),
            ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
            ('inventory', models.PositiveIntegerField(default=0)),
        ], options={'ordering': ['title']}),
        migrations.CreateModel(name='Booking', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('first_name', models.CharField(max_length=100)),
            ('reservation_date', models.DateTimeField()),
            ('number_of_guests', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ('contact_email', models.EmailField(blank=True, max_length=254)),
            ('notes', models.TextField(blank=True)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
        ], options={'ordering': ['reservation_date']}),
    ]
