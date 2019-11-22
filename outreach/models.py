from django.db import models


# Create your models here.
from people.models import Person


class Organization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    num_members = models.IntegerField()
    notes = models.TextField()
    contact = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150, choices=(('Upcoming', 'Upcoming'), ('Ongoing', 'Ongoing'),
                                                       ('Completed', 'Completed')))
    notes = models.TextField()
    community_partner = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='community')
    lafayette_organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='lafayette')
    student_partner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='student')
    faculty_partner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='faculty')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField()
    pulse_date = models.DateField()
    num_volunteers = models.IntegerField()
    notes = models.TextField()
    coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='coordinator')
    contact = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='contact')
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
