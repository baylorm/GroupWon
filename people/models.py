from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)


class Person(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    role = models.CharField(max_length=100, choices=(('Student', 'Student'), ('Faculty', 'Faculty'),
                                                     ('Community Member', 'Community Member')), )

    def __str__(self):
        return self.first + " " + self.last


class Phone(models.Model):
    number = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number


class FacultyType(models.Model):
    type = models.CharField(max_length=100, unique=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.type
