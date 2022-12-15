# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (ChatHistoryView,)

urlpatterns = [
    path('question', ChatHistoryView.as_view()),
]