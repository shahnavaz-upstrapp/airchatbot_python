# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (RegisterView,)

urlpatterns = [
    path('register', RegisterView.as_view()),
]