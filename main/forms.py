from .models import Attendance,Marks,Grade_and_Section,Exams,Subjects
from django import forms
from django.forms import ModelForm
from datetime import date


class date_form(forms.Form):
    date = forms.DateField()

class_choices = list({(str(i.Grade) ,str(i.Grade)) for i in Grade_and_Section.objects.all()})
section_choices = list({(str(i.Section) ,str(i.Section)) for i in Grade_and_Section.objects.all()})
test_choices = list({(str(i.exam_name) ,str(i.exam_name)) for i in Exams.objects.all()})
subject_choices = list({(str(i.subject) ,str(i.subject)) for i in Subjects.objects.all()})


class marks_entry_form(forms.Form):
    Class = forms.ChoiceField(choices=class_choices)
    Section = forms.ChoiceField(choices=section_choices)
    test = forms.ChoiceField(choices=test_choices)
    subject=forms.ChoiceField(choices=subject_choices)


class assign_marks_form(forms.Form):
    Marks_given =  forms.IntegerField()

class exam_form(forms.ModelForm):
    class Meta:
        model =Exams
        fields = '__all__'