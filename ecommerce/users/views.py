from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from users.serializers import UserSerializer
from users.models import User

class UserAPIView(APIView):

    def get(self,request):
        users = User.objects.all()
        user_serialized = UserSerializer(users, many=True)
        return Response(user_serialized.data)
