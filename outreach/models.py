from django.db import models


# Create your models here.
from people.models import Person


class Organization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150, choices=(('Community Organization', 'Community Organization'), ('Club', 'Club'), ('Course', 'Course')))
    num_members = models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of Members')
    notes = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150, choices=(('Upcoming', 'Upcoming'), ('Ongoing', 'Ongoing'),
                                                       ('Completed', 'Completed')))
    notes = models.TextField(blank=True, null=True)
    community_partner = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='community', verbose_name='Community Partner')
    lafayette_organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='lafayette', verbose_name='Lafayette Organization')
    student_partner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='student', verbose_name='Student Partner')
    faculty_partner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='faculty', verbose_name='Faculty Partner')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(blank=True, null=True)
    pulse_date = models.DateField(blank=True, null=True, verbose_name='Pulse Date')
    num_volunteers = models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of Volunteers')
    notes = models.TextField(blank=True, null=True)
    coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='coordinator')
    contact = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='contact')
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
