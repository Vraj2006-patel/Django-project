from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    search=request.GET.get('search')
    if search:
        students = Student.objects.filter(name__icontains = search)
    else:
        students = Student.objects.all()    
    return render(request, 'home.html',{'students':students})

def welcome(request):
    return render(request, 'welcome.html')