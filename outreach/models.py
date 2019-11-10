from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    notes = models.TextField()

