# from django.shortcuts import render
from .models import Student, Book
from .serializers import StudentSerializer, BookSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema # for coreapi


# Create your views here.

# students
# for coreapi; deosn't need 'GET' because it has no request.body
@swagger_auto_schema(methods=['POST'], request_body=StudentSerializer()) 
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
        serializer = StudentSerializer(data=request.data) # get and serialize

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


# student detail
# for coreapi; doesn't need 'GET' because it has no request.body
@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=StudentSerializer()) 
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, student_id):
    """
        Takes in a student_id and returns the http response depending on the http method

        Args:
        student_id: Interger

        Allowed method
        GET - get the detail of a single student
        PUT - Allows you to edit the student detail
        DELETE - This logic deletes the student record from the data base
    """

    try:# get the data from the model
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        error = {
            "message": "failed",
            "errors": f"Student with id {student_id} does not exist"
        }
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        data = { # prepare response data
            "message": "success",
            "data": serializer.data
        } 
        # send the response
        return Response(data, status=status.HTTP_200_OK) 

    elif request.method == "PUT":
        # partial allows for patch updates as well
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            data = {
                "message": "success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

        else:
            error = {
                "message": "failed",
                "errors": serializer.errors
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        context = {"message":"success"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)



# books
# for coreapi; doesn't need 'GET' because it has no request.body
@swagger_auto_schema(methods=['POST'], request_body=BookSerializer()) 
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


# book detail
# for coreapi; doesn't need 'GET' because it has no request.body
@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=BookSerializer()) 
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    """
        Takes in a book_id and returns the http response depending on the http method

        Args:
        book_id: Interger

        Allowed method
        GET - get the detail of a single book
        PUT - Allows you to edit the book detail
        DELETE - This logic deletes the book record from the data base
    """

    try:# get the data from the model
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        error = {
            "message": "failed",
            "errors": f"Student with id {book_id} does not exist"
        }
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        data = { # prepare response data
            "message": "success",
            "data": serializer.data
        } 
        # send the response
        return Response(data, status=status.HTTP_200_OK) 

    elif request.method == "PUT":
        # partial allows for patch updates as well
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            data = {
                "message": "success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

        else:
            error = {
                "message": "failed",
                "errors": serializer.errors
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        context = {"message":"success"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def list_cohort(request):
    if request.method == 'GET':
        # getting values for a field in django model
        cohorts = Student.objects.values_list('cohort', flat=True)
        data = {cohort:{
            "count": Student.objects.filter(cohort=cohort).count(),
            "data": Student.objects.filter(cohort=cohort).values()
            } for cohort in cohorts}
        print(cohorts)

        context = {"message": "success", "data": data} 
        return Response(context, status=status.HTTP_200_OK)
