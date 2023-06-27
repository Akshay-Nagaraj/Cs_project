from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from datetime import date
from django.contrib.auth.models import User,Group
from .models import Teacher,Attendance,Grade_and_Section,Student,Marks,Exams,Subjects
from .forms import marks_entry_form,assign_marks_form,exam_form

def teach_Dash(request):
    return render(request,'teachers.html',context={})

def base(request):
    if request.user.is_authenticated:
        if Teacher.objects.all().filter(user = request.user).exists() or request.user.is_superuser:
            return redirect('/home/teachers')
        else:
            return render(request, 'base.html',context={})
    else:
        return redirect('/home/signin')


 
def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request,'registration.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'registration.html', {'form':form})
    
    
 
def signout(request):
    logout(request)
    return redirect('/home/signin/')

def to_base(request):
    return redirect('/home')


def dummy(request):
    return render(request,'dummy.html',context={})
def teach_attendance(request):
    req=[]
    if Teacher.objects.all().filter(user=request.user,is_classTeacher=True).exists():
        current = Teacher.objects.get(user=request.user)
        g_s = Grade_and_Section.objects.get(class_teacher=current)
        Attendance.objects.bulk_create([Attendance(student = i,date=date.today(),grade_and_section=g_s) for i in Student.objects.all().filter(grade_and_section=g_s) if not Attendance.objects.all().filter(student=i,date=date.today()).exists()])
        data = Attendance.objects.all().filter(grade_and_section=g_s,date=date.today())
        return render(request, 'attendance.html', context={'data':data})
    else:
        return redirect('/home')

def morning_absent(request, id):
    stu = Attendance.objects.get(id=id)
    stu.morning = False
    stu.save()
    return redirect('/home/teachers/attendance')

def afternoon_absent(request,id):
    stu = Attendance.objects.get(id=id)
    stu.afternoon = False
    stu.save()
    return redirect('/home/teachers/attendance')

def morning_present(request, id):
    stu = Attendance.objects.get(id=id)
    stu.morning = True
    stu.save()
    return redirect('/home/teachers/attendance')

def afternoon_present(request,id):
    stu = Attendance.objects.get(id=id)
    stu.afternoon = True
    stu.save()
    return redirect('/home/teachers/attendance')
def marks_page(request):
    form = marks_entry_form(request.POST)
    global marks_form
    marks_form = assign_marks_form(request.POST)
    teacher = Teacher.objects.get(user=request.user)
    student_list=None
    marks_list=None
    if request.method == 'POST':
        if form.is_valid():
            g = form.cleaned_data.get('Class')
            s = form.cleaned_data.get('Section')
            g_s = Grade_and_Section.objects.get(Grade=g,Section=s)
            student_list = Student.objects.all().filter(grade_and_section=g_s)
            Marks.objects.bulk_create([Marks(exam=Exams.objects.get(exam_name=form.cleaned_data.get('test')),subject=Subjects.objects.get(subject=form.cleaned_data.get('subject')),student=i) for i in student_list if not Marks.objects.all().filter(student=i,exam=Exams.objects.get(exam_name=form.cleaned_data.get('test')),subject=Subjects.objects.get(subject=form.cleaned_data.get('subject'))).exists()])
            marks_list=[Marks.objects.get(exam=Exams.objects.get(exam_name=form.cleaned_data.get('test')), student= i,subject=Subjects.objects.get(subject=form.cleaned_data.get('subject')) ) for i in student_list]
        else:
            return redirect('/home/teachers/marks')
    context={'student_list':student_list,'form':form,'marks_list':marks_list,'marks_entry_form':marks_entry_form,'marks_form':marks_form}
    return render(request, 'marks_entry.html',context)

def marks_edit(request,id):
    marks_form = assign_marks_form(request.POST)
    if request.method =='POST':
        if marks_form.is_valid():
            marks = marks_form.cleaned_data.get('Marks_given')
            m = Marks.objects.get(id=id)
            m.assigned_marks=marks
            m.save()
        else:
            marks_form = assign_marks_form(request.POST)
    return redirect('/home/teachers/marks')

def create_exam(request):
    if request.user.is_superuser:
        form = exam_form(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
            else:
                form = exam_form()
        return render(request, 'addExam.html' ,context={'form':form})


