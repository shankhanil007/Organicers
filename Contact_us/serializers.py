from .models import *
from rest_framework import serializers

class Contact_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'