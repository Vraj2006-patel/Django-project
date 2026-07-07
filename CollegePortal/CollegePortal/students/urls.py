from django.urls import path

from .views import student_list, delete_student

from .views import add_student, edit_student, student_details

urlpatterns = [

    path(
        "",
        student_list,
        name="student_list"
    ),

    path(
        "add/",
        add_student,
        name="add_student"
    ),

    path(
    "edit/<int:id>/",
    edit_student,
    name="edit_student"
),

path(
    "details/<int:id>/",
    student_details,
    name="student_details"
),

path(
    "delete/<int:id>/",
    delete_student,
    name="delete_student"
),
]