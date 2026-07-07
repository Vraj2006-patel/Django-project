from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    email = models.EmailField()