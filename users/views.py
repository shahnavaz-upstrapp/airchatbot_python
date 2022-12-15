# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import RegisterSerializer

class RegisterView(APIView):
  def post(self, request):
    
    serializer = RegisterSerializer(data=request.data)
   
    if serializer.is_valid():
      user_obj = User.objects.filter(email=serializer.data.get('email')).first()
     
      if not user_obj:
        user_obj = User()
        user_obj.full_name = serializer.data.get('full_name')
        user_obj.email = serializer.data.get('email')
        user_obj.phone_number = serializer.data.get('phone_number')
        user_obj.save()
      
      token = Token.objects.get_or_create(user=user_obj)[0]
      print("token: ", token)
      
      response_data = dict()
      response_data['token'] = "Token {}".format(token)
      
      return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)