from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Student
# Create your views here.

def Hello(request):
    return HttpResponse('Welcome to Django')

def Students(request):
    context = {'student': Students}
    return render(request, 'student.html', context)

def createStudents(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        department = request.POST['mobile']
        semester = request.POST['semester']
        
        student = Student(first_name=first_name, last_name=last_name, email=email, mobile=mobile, department=department, semester=semester)
        student.save()
        return redirect('/Students/')
    else:
        return render(request, 'createstudent.html')
        