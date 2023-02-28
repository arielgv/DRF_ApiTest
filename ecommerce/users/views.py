from django.shortcuts import render
from rest_framework import status
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
        return Response(user_serialized.data, status = status.HTTP_200_OK)

    elif request.method =='POST':
        user_serialized = UserSerializer(data = request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(UserSerializer(User.objects.all(), many=True).data, status = status.HTTP_201_CREATED)
        return Response(user_serialized.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def one_user_api_view(request,pk):
    # queryset
    user = User.objects.filter(id = pk).first()
    # validation
    if user :
        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response (user_serializer.data, status= status.HTTP_200_OK)
        
        # update
        if request.method == 'PUT':

            modification = UserSerializer(user, data = request.data)
            if modification.is_valid():
                modification.save()
                return Response(modification.data, status = status.HTTP_202_ACCEPTED)
            else:
                return Response(modification.errors, status = status.HTTP_400_BAD_REQUEST)
        # delete            
        if request.method == 'DELETE':

            user.delete()
            return Response('Deleted', status= status.HTTP_202_ACCEPTED)
    return Response({'Message' : 'User not found.'}, status = status.HTTP_400_BAD_REQUEST)
