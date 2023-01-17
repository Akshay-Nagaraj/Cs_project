from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group

def base(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name = 'Teachers').exists():
            return render(request, 'teachers.html',context={})
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

def teach_Dash(request):
    return render(request,'teacher.html',context={})
def dummy(request):
    return render(request,'dummy.html',context={})