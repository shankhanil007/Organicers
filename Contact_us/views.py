from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact_Us
from .serializers import Contact_UsSerializer
from . import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class Contact_UsList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        Contact1 = Contact_Us.objects.all()
        serializer = Contact_UsSerializer(Contact1,many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = Contact_UsSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST',])
# def api_detail_app_view(request):
#          Contact1 = Contact_Us.objects.all()
#          serializer = Contact_UsSerializer(Contact1, data = request.data)
#
#          print(request.data)
#
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#          return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
