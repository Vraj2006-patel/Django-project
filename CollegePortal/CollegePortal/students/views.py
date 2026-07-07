from django.shortcuts import render

from .models import Student


from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializers
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializers
    permission_classes=[IsAuthenticated]
@login_required
def student_list(request):

    search = request.GET.get("search")

    if search:

        students = Student.objects.filter(

            Q(name__icontains=search) |

            Q(department__icontains=search) |

            Q(city__icontains=search)

        )

    else:

        students = Student.objects.all()

    return render(
        request,
        "students/list.html",
        {"students": students, 'search':search}
    )

from django.shortcuts import redirect


@login_required
def add_student(request):

    if request.method == "POST":

        Student.objects.create(

            name=request.POST["name"],

            email=request.POST["email"],

            phone=request.POST["phone"],

            department=request.POST["department"],

            semester=request.POST["semester"],

            cgpa=request.POST["cgpa"],

            city=request.POST["city"]
        )

        return redirect("student_list")

    return render(

        request,

        "students/add.html"
    )

from django.shortcuts import get_object_or_404

@login_required
def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        student.name = request.POST["name"]

        student.email = request.POST["email"]

        student.phone = request.POST["phone"]

        student.department = request.POST["department"]

        student.semester = request.POST["semester"]

        student.cgpa = request.POST["cgpa"]

        student.city = request.POST["city"]

        student.save()

        return redirect(
            "student_list"
        )

    return render(

        request,

        "students/edit.html",

        {"student": student}
    )

@login_required
def student_details(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    return render(
        request,
        "students/details.html",
        {"student": student}
    )

@login_required
def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        student.delete()

        return redirect(
            "student_list"
        )

    return render(
        request,
        "students/delete.html",
        {"student": student}
    )