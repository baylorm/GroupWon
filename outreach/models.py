from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    notes = models.TextField()


class Organization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    num_members = models.IntegerField()
    notes = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    pulse_date = models.DateField()
    num_volunteers = models.IntegerField()
    notes = models.TextField()
