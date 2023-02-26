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



@api_view(['GET','PUT','DELETE'])
def one_user_api_view(request,pk):

    if request.method == 'GET':

        user = User.objects.filter(id=pk).first()
        print(user)
        user_serializer = UserSerializer(user)
        return Response (user_serializer.data)
    
    if request.method == 'PUT':

        user = User.objects.filter(id=pk).first()
        modification = UserSerializer(user, data = request.data)
        if modification.is_valid():
            modification.save()
            return Response(modification.data)
        else:
            return Response(modification.errors)
        
    if request.method == 'DELETE':
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response('Deleted')
