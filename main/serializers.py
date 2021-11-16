from rest_framework import serializers
from .models import Student, Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


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