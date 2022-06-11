from django.contrib import admin
from django.urls import path
from .views import Hello,Home

urlpatterns = [
    path('Hello/', Hello, name='Hello'),
    path('', Home, name='Home')
]