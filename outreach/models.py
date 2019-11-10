from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    num_members = models.IntegerField()
    notes = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150, choices=(('Upcoming', 'Upcoming'), ('Ongoing', 'Ongoing'),
                                                       ('Completed', 'Completed')))
    notes = models.TextField()
    community_partner = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True, related_name='community')
    lafayette_organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True, related_name='lafayette')


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField()
    pulse_date = models.DateField()
    num_volunteers = models.IntegerField()
    notes = models.TextField()
