"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from Category_Auth import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="login/index.html")),
    # path('', views.home),
    path('admin/', admin.site.urls),
    path('Category', views.CategoryList.as_view()),
    path('auth/', include('Category_Auth.urls')),
    path('verify/', include('otp.urls')),
    path('accounts/', include('allauth.urls')),
    path('book/events',include('event.urls')),
    path('contact/',include('Contact_us.urls')),
]
