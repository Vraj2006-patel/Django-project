from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    department = models.CharField(max_length=50)

    semester = models.IntegerField()

    cgpa = models.FloatField()

    city = models.CharField(max_length=50)

    def __str__(self):

        return self.name