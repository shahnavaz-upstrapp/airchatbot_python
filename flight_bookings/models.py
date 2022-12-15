from django.db import models
from flights.models import Flight
from users.models import User

class FlightBooking(models.Model):
    booking_id = models.CharField(max_length = 255)

    booking_date = models.DateTimeField(null=True, blank = True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
  
    fare = models.IntegerField(null=True, blank = True, default=0)
    booking_status = models.IntegerField(null=True, blank = True, default=0)
    seat_no = models.IntegerField(null=True, blank = True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "FlightBooking"
        verbose_name_plural = "FlightBookings"
        ordering = ["created_at"]
        
    def __str__(self):
        return self.booking_id
