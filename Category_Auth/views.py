from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
def home(request):
    return JsonResponse({'foo':'bar'})
class CategoryList(APIView):

    def get(self, request):
        Category1 = Category.objects.all()
        serializer = CategorySerializer(Category1,many=True)
        return Response(serializer.data)
