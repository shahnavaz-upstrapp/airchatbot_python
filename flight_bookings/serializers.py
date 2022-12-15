# todo/todo_api/serializers.py
from rest_framework import serializers

class FlightBookingSerializer(serializers.Serializer):
    booking_date = serializers.CharField(required=True)
    flight_id = serializers.IntegerField(required=True)

class CancelFlightBookingSerializer(serializers.Serializer):
    booking_id = serializers.CharField(required=True)
