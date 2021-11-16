from rest_framework import serializers
from .models import Student, Book

class StudentSerializer(serializers.ModelSerializer):
    study_books = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = [  #'__all__'#
            "id",   
            "name",
            "gender",
            "dob",
            "cohort",
            "study_books"                     
        ]        


class BookSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField()
    class Meta:
        model = Book                             
        fields = [
            "id",
            "title",
            "student",
            "student_name",
            "author",
            "body",                       
            "isbn",
            "date"
        ]