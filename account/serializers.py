from rest_framework import serializers
from .models import CustomUser

# Best Practice; so whenever you change User model name, 
#   - you don't have to do so everywhere just in settings at AUTH_USER_MODEL
# from .models import get_user_model
# User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CustomUser
        fields = '__all__'