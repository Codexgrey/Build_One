# from django.shortcuts import render
# Create your views here.
from .models import Student
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        return Response({}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response({}, status=status.HTTP_200_OK)