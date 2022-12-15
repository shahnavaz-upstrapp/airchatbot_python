# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters, generics, permissions, views

from .models import FlightBooking
from .serializers import FlightBookingSerializer, CancelFlightBookingSerializer
import datetime


class AddFlightBookingView(APIView):
  permission_classes = [permissions.IsAuthenticated]
   
  def post(self, request):
    
    serializer = FlightBookingSerializer(data=request.data)
   
    if serializer.is_valid():
      booking_date = serializer.data.get('booking_date')
      flight_id = serializer.data.get('flight_id')
      
      booking_date = [int(ele) for ele in booking_date.split("/")]

      booking_date = datetime.date(booking_date[2], booking_date[1], booking_date[0])

      booking_obj = FlightBooking()
      booking_obj.booking_date = booking_date
      booking_obj.flight_id = flight_id
      booking_obj.booked_by = request.user
      booking_obj.booking_status = 1
      booking_obj.save()
      booking_obj.booking_id = "BK{}{}".format(booking_obj.flight.flight_number ,booking_obj.pk)
      booking_obj.save()
    
      response_data = dict()
      response_data['booking_id'] = booking_obj.booking_id
      
      return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  

class MyFlightBookingsView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):

			flight_objs = FlightBooking.objects.filter(booked_by=request.user.id)
		
			booking_list = list()
			
			for ele in flight_objs:
				data_info = dict()
				data_info['id'] = ele.pk
				data_info['booking_id'] = ele.booking_id
				data_info['booking_date'] = ele.booking_date
				data_info['booking_status'] = ele.booking_status
				data_info['created_at'] = ele.created_at
				flight_details = dict()
				flight_details['flight_number'] = ele.flight.flight_number
				flight_details['airline_name'] = ele.flight.airline_name
				flight_details['airline_code'] = ele.flight.airline_code
				flight_details['origin_location'] = ele.flight.origin_location
				flight_details['origin_airport_name'] = ele.flight.origin_airport_name
				flight_details['origin_airport_code'] = ele.flight.origin_airport_code
				flight_details['origin_airport_time'] = ele.flight.origin_airport_time
				flight_details['origin_airport_est_time'] = ele.flight.origin_airport_est_time
				flight_details['destination_location'] = ele.flight.destination_location
				flight_details['destination_airport_name'] = ele.flight.destination_airport_name
				flight_details['destination_airport_code'] = ele.flight.destination_airport_code
				flight_details['destination_airport_est_time'] = ele.flight.destination_airport_est_time
				flight_details['fare'] = ele.flight.fare
				flight_details['status'] = ele.flight.status
				data_info['flight'] = flight_details
    
				booking_list.append(data_info)

			response_data = dict()
			response_data['booking_list'] = booking_list

			return Response(response_data, status=status.HTTP_200_OK)


class CancelFlightBookingView(APIView):
  permission_classes = [permissions.IsAuthenticated]
   
  def post(self, request):
    
    serializer = CancelFlightBookingSerializer(data=request.data)
   
    if serializer.is_valid():
      booking_id = serializer.data.get('booking_id')
      
      booking_obj = FlightBooking.objects.filter(booking_id=booking_id, booked_by=request.user.id).first()
      if not booking_obj:
        return Response("Data not found", status=status.HTTP_400_BAD_REQUEST)

      if booking_obj.booking_status == 2:
        return Response("Already Cancelled", status=status.HTTP_400_BAD_REQUEST)

      booking_obj.booking_status = 2
      booking_obj.save()
    
      response_data = dict()
      response_data['booking_id'] = booking_obj.booking_id
      response_data['booking_status'] = booking_obj.booking_status

      return Response(response_data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


class MyFlightBookingByIdView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request, booking_id):
    booking_obj = FlightBooking.objects.filter(booking_id=booking_id, booked_by=request.user.id).first()
   
    if not booking_obj:
      return Response("Data not found", status=status.HTTP_400_BAD_REQUEST)
   
    booking_details = dict()
    booking_details['id'] = booking_obj.id
    booking_details['booking_id'] = booking_obj.booking_id
    booking_details['booking_date'] = booking_obj.booking_date
    booking_details['booking_status'] = booking_obj.booking_status
    booking_details['created_at'] = booking_obj.created_at
    
    status_message_dict = {}
    status_message_dict[1] = "On Time"
    status_message_dict[2] = "Delayed"
    status_message_dict[3] = "Cancelled"
    
    flight_details = dict()
    flight_details['flight_number'] = booking_obj.flight.flight_number
    flight_details['airline_name'] = booking_obj.flight.airline_name
    flight_details['airline_code'] = booking_obj.flight.airline_code
    flight_details['origin_location'] = booking_obj.flight.origin_location
    flight_details['origin_airport_name'] = booking_obj.flight.origin_airport_name
    flight_details['origin_airport_code'] = booking_obj.flight.origin_airport_code
    flight_details['origin_airport_time'] = booking_obj.flight.origin_airport_time
    flight_details['origin_airport_est_time'] = booking_obj.flight.origin_airport_est_time
    flight_details['destination_location'] = booking_obj.flight.destination_location
    flight_details['destination_airport_name'] = booking_obj.flight.destination_airport_name
    flight_details['destination_airport_code'] = booking_obj.flight.destination_airport_code
    flight_details['destination_airport_time'] = booking_obj.flight.destination_airport_time
    flight_details['destination_airport_est_time'] = booking_obj.flight.destination_airport_est_time
    flight_details['fare'] = booking_obj.flight.fare
    flight_details['status'] = booking_obj.flight.status
    flight_details['status_message'] = status_message_dict.get(booking_obj.flight.status, 'on Time')
    
    booking_details['flight'] = flight_details

    response_data = dict()
    response_data['booking_details'] = booking_details
    return Response(response_data, status=status.HTTP_200_OK)
