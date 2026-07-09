
# Register your models here.
from django.contrib import admin
from .models import Student

# This displays student fields in a neat table format within the dashboard
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'semester', 'email')
    search_fields = ('name', 'email')
