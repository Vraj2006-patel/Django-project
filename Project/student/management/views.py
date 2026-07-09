# Make sure line 1 includes 'redirect' and 'get_object_or_404'
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
        else:
            # If form has validation errors, it falls through to render below with errors
            print("Form Errors:", form.errors) # This prints errors to your terminal
    else:
        form = UserCreationForm()
        
    # Ensure this return statement is completely outside the if/else block!
    return render(request, 'signup.html', {'form': form})

def loginacc(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_list')
        else:
            # Prints validation failures directly to your terminal
            print("Login Form Errors:", form.errors) 
    else:
        form = AuthenticationForm()
        
    # Make sure this return statement sits completely outside the if/else block!
    return render(request, 'login.html', {'form': form})
def logoutacc(request):
    logout(request)
    return render(request, 'logout.html')  

def student_list_view(request):
    return render(request,'student_list.html')

@login_required(login_url='login')
def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("STUDENT SAVED SUCCESSFULLY!")  # Will show in terminal
            return redirect('student_list')
        else:
            print("FORM ERRORS:", form.errors)  # Will print errors to terminal
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required(login_url='login')
def edit_student_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            print(f"STUDENT {id} UPDATED SUCCESSFULLY!")
            return redirect('student_list')
        else:
            print("EDIT FORM ERRORS:", form.errors)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

@login_required(login_url='login')
def delete_student_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        print(f"STUDENT {id} DELETED SUCCESSFULLY!")
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})
