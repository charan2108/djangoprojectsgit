from django.contrib import admin
from django.urls import path
from .views import Hello, Students,createStudents


urlpatterns = [
   path('Hello/', Hello, name='Hello'),
   path('Students/', Students, name='Students'),
   path('createStudents/', createStudents, name='createStudents')
]
