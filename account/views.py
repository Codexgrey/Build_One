# from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password

# Create your views here.

# CustomUser
# for coreapi; deosn't need 'GET' because it has no request.body
@swagger_auto_schema(methods=['POST'], request_body=CustomUserSerializer()) 
@api_view(['GET', 'POST'])
def user_accounts(request):
    if request.method == 'GET':
        # getting all students data and serializing it
        # all_Users = CustomUser.objects.all()
        all_Users = CustomUser.objects.filter(is_active=True)
        serializer = CustomUserSerializer(all_Users, many=True)

        # parsing data into dict for response
        data = {
            "message": "success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # get and deserialize data
        serializer = CustomUserSerializer(data=request.data)

        # validating data and saving if valid, else = error
        if serializer.is_valid():
            # hashing password
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password']
            )

            # new user serialized after being validated
            user = CustomUser.objects.create(**serializer.validated_data)            
            user_serializer = CustomUserSerializer(user)

            # new user sent as data
            data = {
                "message": "success",
                "data": user_serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            error = {
                "message": "failed",
                "errors": serializer.errors
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)