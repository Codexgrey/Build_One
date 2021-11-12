# from django.shortcuts import render
# Create your views here.
from .models import Student, Book
from .serializers import StudentSerializer, BookSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        # getting all students data and serializing it
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)

        # parsing data into dict for response
        data = {
            "message": "success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # get and deserialize data
        serializer = StudentSerializer(data=request.data)

        # validating data and saving if valid, else = error
        if serializer.is_valid():
            serializer.save()

            data = {
                "message": "success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            error = {
                "message": "failed",
                "errors": serializer.errors
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        # getting all students data and serializing it
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)

        # parsing data into dict for response
        data = {
            "message": "success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # get and deserialize data
        serializer = BookSerializer(data=request.data)

        # validating data and saving if valid, else = error
        if serializer.is_valid():
            serializer.save()

            data = {
                "message": "success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            error = {
                "message": "failed",
                "errors": serializer.errors
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)