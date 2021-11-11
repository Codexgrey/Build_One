from rest_framework import serializers
from .models import Student, Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'