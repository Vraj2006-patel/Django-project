from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    stuid=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    result=models.CharField()
    