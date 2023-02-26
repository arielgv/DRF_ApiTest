from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from users.serializers import UserSerializer
from users.models import User


@api_view(['GET','POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        user_serialized = UserSerializer(users, many=True)
        return Response(user_serialized.data)

    elif request.method =='POST':
        user_serialized = UserSerializer(data = request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(UserSerializer(User.objects.all(), many=True).data)
        return Response(user_serialized.errors)    




    