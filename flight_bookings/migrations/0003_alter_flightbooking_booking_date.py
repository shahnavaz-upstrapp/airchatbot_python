# Generated by Django 4.1.4 on 2022-12-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_bookings', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightbooking',
            name='booking_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]