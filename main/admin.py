from django.contrib import admin
from .models import students
from.models import singup
from.models import ClassStudent
from.models import StudentAdmission
# Register your models here.
admin.site.register(students)
admin.site.register(singup)
admin.site.register(ClassStudent)
admin.site.register(StudentAdmission)