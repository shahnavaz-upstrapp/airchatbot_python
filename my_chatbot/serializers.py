# todo/todo_api/serializers.py
from rest_framework import serializers

class ChatQuestionSerializer(serializers.Serializer):
    action_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    subject = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    message = serializers.CharField(required=False)