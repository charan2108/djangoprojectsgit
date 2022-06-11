from django.contrib import admin
from . models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name', 'last_name', 'email', 'mobile','department','semester')
    list_display_links =('id', 'first_name', 'last_name', 'email', 'mobile','department','semester')

admin.site.register(Student, StudentAdmin)