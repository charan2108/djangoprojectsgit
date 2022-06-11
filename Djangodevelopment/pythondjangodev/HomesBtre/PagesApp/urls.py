from django.contrib import admin
from django.urls import path,include

from .views import hello, home, about

urlpatterns = [
    path('hello/', hello ,name='hello'),
    path('',home,name='home'),
    path('about/', about, name='about')
]
