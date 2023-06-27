from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=254,null=True)
    is_classTeacher = models.BooleanField(default=False)

class Grade_and_Section(models.Model):
    Grade = models.PositiveSmallIntegerField()
    Section = models.CharField(max_length=1)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    

class Student(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    DOB = models.DateField(max_length=254)
    grade_and_section =  models.ForeignKey(Grade_and_Section, on_delete=models.CASCADE,null=False,default=None)
    roll_no = models.PositiveSmallIntegerField(null=False,default=None)
    subject_list = models.CharField(max_length=254,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields = ['grade_and_section','roll_no'],name='Unique Roll')
        ]

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade_and_section = models.ForeignKey(Grade_and_Section, on_delete=models.CASCADE)
    date = models.DateField()
    morning  = models.BooleanField(default=True,null=True)
    afternoon = models.BooleanField(default=True,null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['student','date'],name='Unique attendance')
        ]

class Subjects(models.Model):
    course = models.ForeignKey(Grade_and_Section, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=254)
    is_core = models.BooleanField()
    is_elective = models.BooleanField()

class Exams(models.Model):
    exam_name = models.CharField(max_length=254)
    course = models.ForeignKey(Grade_and_Section, on_delete=models.CASCADE,default=None)
    max_marks = models.IntegerField(default=None)

class Marks(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigned_marks = models.IntegerField(null=True)
    class Meta:
        constraints =[ 
            models.UniqueConstraint(fields = ['exam','subject','student'],name='Unique marks entry')
        ]