from django.urls import path, include
from .views import Contact_UsList

app_name = 'app'

urlpatterns = [
    path("", Contact_UsList.as_view())
]