# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (AvailableFlightsView,SeederView)

urlpatterns = [
    path('seeder', SeederView.as_view()),
    path('available-flights', AvailableFlightsView.as_view()),
]