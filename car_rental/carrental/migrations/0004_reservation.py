# Generated by Django 3.1.12 on 2021-06-22 08:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrental', '0003_cars_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_booking', models.DateField(editable=False)),
                ('end_time_booking', models.DateField(editable=False)),
                ('isactive', models.BooleanField(default=True)),
                ('isrented', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1)], verbose_name='Quantity')),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrental.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
