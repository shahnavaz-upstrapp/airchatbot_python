# Generated by Django 4.1.4 on 2022-12-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=255)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('fare', models.IntegerField(blank=True, default=0, null=True)),
                ('booking_status', models.IntegerField(blank=True, default=0, null=True)),
                ('seat_no', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'FlightBooking',
                'verbose_name_plural': 'FlightBookings',
                'ordering': ['created_at'],
            },
        ),
    ]
