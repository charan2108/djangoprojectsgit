from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(index):
    return HttpResponse('<h1>Hello World</h1>')

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')