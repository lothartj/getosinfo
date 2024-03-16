from django.contrib import admin
from django.urls import path, include
from .views import getosinfo
urlpatterns = [
    path('', getosinfo, name='getosinfo'),
]
