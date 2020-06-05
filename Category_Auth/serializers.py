from . models import  Category
from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        # fields = {'id','username','password','first_name','last_name','phone',}
        fields = '__all__'