from django.shortcuts import render
from django.contrib import messages
from students.models import Student

from django.db.models import Avg

def home(request):

    return render(

        request,

        "home.html"
    )

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate

from django.contrib.auth import login


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(

            request,

            username=username,

            password=password
        )

        if user:

            login(request, user)

            return redirect("dashboard")
    
    else:

        messages.error(

            request,

            "Invalid Username or Password"
        )

    return render(

        request,

        "login.html"
    )


from django.contrib.auth import logout


def logout_view(request):

    logout(request)

    return redirect("login")

from django.contrib.auth.decorators import login_required

from students.models import Student

from django.db.models import Avg

@login_required
def dashboard(request):

    total_students = Student.objects.count()

    departments = Student.objects.values(
        "department"
    ).distinct().count()

    average = Student.objects.aggregate(
        Avg("cgpa")
    )

    topper = Student.objects.order_by(
        "-cgpa"
    ).first()

    recent_students = Student.objects.order_by(
        "-id"
    )[:5]

    context = {

        "total_students": total_students,

        "departments": departments,

        "average_cgpa": round(
            average["cgpa__avg"],
            2
        ),

        "topper": topper,

        "recent_students": recent_students
    }

    return render(
        request,
        "dashboard.html",
        context
    )