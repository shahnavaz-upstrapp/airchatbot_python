# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters, generics, permissions, views
from .models import Flight

import datetime


class AvailableFlightsView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
			departure = request.GET.get('departure', None)
			arrival  = request.GET.get('arrival', None)
			from_date  = request.GET.get('from_date', None) # dd/mm/yyyy

			flight_objs = Flight.objects.all()
			if departure:
				flight_objs = flight_objs.filter(origin_location__icontains=departure)

			if arrival:
				flight_objs = flight_objs.filter(destination_location__icontains=arrival)
			
			if from_date:
				from_date_list = [int(ele) for ele in from_date.split("/")]
				
				
				t_date = datetime.date(from_date_list[2], from_date_list[1], from_date_list[0])
				t_weekday = str(t_date.weekday())
				flight_objs = flight_objs.filter(weekdays__icontains=t_weekday)
				
				print("t_weekday: ", t_weekday)

		
			flight_list = list()
			
			for ele in flight_objs:
				data_info = dict()
				data_info['id'] = ele.pk
				data_info['flight_number'] = ele.flight_number
				data_info['airline_name'] = ele.airline_name
				data_info['airline_code'] = ele.airline_code
				data_info['origin_location'] = ele.origin_location
				data_info['origin_airport_name'] = ele.origin_airport_name
				data_info['origin_airport_code'] = ele.origin_airport_code
				data_info['origin_airport_time'] = ele.origin_airport_time
				data_info['origin_airport_est_time'] = ele.origin_airport_est_time
				data_info['destination_location'] = ele.destination_location
				data_info['destination_airport_name'] = ele.destination_airport_name
				data_info['destination_airport_code'] = ele.destination_airport_code
				data_info['destination_airport_time'] = ele.destination_airport_time
				data_info['destination_airport_est_time'] = ele.destination_airport_est_time
				data_info['weekdays'] = ele.weekdays
				data_info['fare'] = ele.fare
				data_info['status'] = ele.status
				data_info['seats'] = ele.seats
				flight_list.append(data_info)

			response_data = dict()
			response_data['flight_list'] = flight_list
			response_data['from_date'] = from_date
			response_data['departure'] = departure
			response_data['arrival'] = arrival

			return Response(response_data, status=status.HTTP_200_OK)