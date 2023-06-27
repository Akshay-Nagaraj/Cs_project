from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Teacher,Student,Attendance,Grade_and_Section,Subjects,Marks,Exams,Marks


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade_and_Section)
admin.site.register(Attendance)
admin.site.register(Subjects)
admin.site.register(Exams)
admin.site.register(Marks)