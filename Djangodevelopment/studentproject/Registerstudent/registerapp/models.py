from django.db import models

# Create your models here.
class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    mobile = models.TextField(max_length=10)
    department = models.CharField(max_length=15)
    semester = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.first_name