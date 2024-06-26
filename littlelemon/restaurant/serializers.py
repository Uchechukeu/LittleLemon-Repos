from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'      
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'