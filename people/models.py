from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)


class Person(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    email = models.EmailField()
    role = models.CharField(max_length=100)


class Phone(models.Model):
    number = models.IntegerField()


class FacultyType(models.Model):
    type = models.CharField(max_length=100)