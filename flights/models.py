from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length = 255)

    airline_name = models.CharField(max_length = 255)
    airline_code = models.CharField(max_length = 255)
    
    origin_location = models.CharField(max_length = 255, null=True, blank = True)
    origin_airport_name = models.CharField(max_length = 255, null=True, blank = True)
    origin_airport_code = models.CharField(max_length = 255, null=True, blank = True)
    origin_airport_time = models.DateTimeField(null=True, blank = True)
    origin_airport_est_time = models.DateTimeField(null=True, blank = True)

    destination_location = models.CharField(max_length = 255, null=True, blank = True)
    destination_airport_name = models.CharField(max_length = 255, null=True, blank = True)
    destination_airport_code = models.CharField(max_length = 255, null=True, blank = True)
    destination_airport_time = models.DateTimeField(null=True, blank = True)
    destination_airport_est_time = models.DateTimeField(null=True, blank = True)

    weekdays = models.CharField(null=True, blank = True, max_length = 255)

    fare = models.IntegerField(null=True, blank = True, default=0)

    status = models.IntegerField(null=True, blank = True, default=0)

    seats = models.IntegerField(null=True, blank = True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"
        ordering = ["created_at"]
        
    def __str__(self):
        return "{}({})-{}".format(self.airline_name, self.airline_code, self.flight_number)
