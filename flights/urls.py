# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (AvailableFlightsView,)

urlpatterns = [
    path('available-flights', AvailableFlightsView.as_view()),
]