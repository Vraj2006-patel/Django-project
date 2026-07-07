from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Student

# Create your views here.
def students(request):
    s = Student.objects.all()
    return render(request, 'list.html', {'s':s})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form':form})
        
def loginacc(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.POST['password'])
        if user is None:
            error = 'The Username or Password is incorrect'
            return render(request, 'login.html',{'error':error})
        else:
            login(request, user)
            return redirect('home')

def logoutacc(request):
    logout(request)
    return redirect('home')

def add(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        student= Student()
        student.name=request.POST['name']
        student.branch=request.POST['branch']
        student.sem=request.POST['sem']
        student.email=request.POST['email']
        student.save()
        return redirect('students')
    
def edit(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        return render(request,'edit.html',{'student':student})
    else:
        student= Student()
        student.name=request.POST['name']
        student.branch=request.POST['branch']
        student.sem=request.POST['sem']
        student.email=request.POST['email']
        student.save()
        return redirect('students')
    
def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')    
