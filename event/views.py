from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny

class EventList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        Event1 = Event.objects.all()
        serializer = EventSerializer(Event1,many=True)
        return Response(serializer.data)