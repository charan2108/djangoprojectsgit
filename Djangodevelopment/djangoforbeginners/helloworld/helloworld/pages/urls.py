from django.contrib import admin
from django.urls import path
from .views import Hello , HomePageView,AboutPageView

urlpatterns = [
  path('Hello/', Hello, name='Hello'),
  path('', HomePageView.as_view(), name='home'),
  path('about/', AboutPageView.as_view(), name='about')

]
