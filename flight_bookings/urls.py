# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (AddFlightBookingView,CancelFlightBookingView, MyFlightBookingsView, MyFlightBookingByIdView)

urlpatterns = [
  path('add', AddFlightBookingView.as_view()),
  path('my-bookings', MyFlightBookingsView.as_view()),
	path('cancel', CancelFlightBookingView.as_view()),
  path('my-bookings/<str:booking_id>', MyFlightBookingByIdView.as_view()),

 

]