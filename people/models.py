from django.db import models
from phone_field import PhoneField


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class FacultyType(models.Model):
    type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type


class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=(('Student', 'Student'), ('Faculty', 'Faculty'),
                                                    ('Community Member', 'Community Member')))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    faculty_type = models.ForeignKey(FacultyType, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first + " " + self.last


class Phone(models.Model):
    number = PhoneField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.number)
