# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatHistory
from .serializers import ChatQuestionSerializer

class ChatHistoryView(APIView):
    # 1. List all
    def get(self, request):
        data = ChatHistory.objects.all()
        serializer = ChatQuestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'question': request.data.get('question'), 
        }
        serializer = ChatQuestionSerializer(data=data)
        if serializer.is_valid():
        #     serializer.save()
            response_data = dict()
            response_data['question'] = request.data.get('question')
            response_data['answer'] = "ans"
            
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)