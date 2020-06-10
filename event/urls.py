from django.urls import path, include
from .views import EventList

urlpatterns =[
    path("", EventList.as_view()),
]