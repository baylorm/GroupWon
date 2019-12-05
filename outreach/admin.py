from dal import autocomplete
from django.contrib import admin
from .models import Project, Organization, Event
from django import forms


def mark_upcoming(modeladmin, request, queryset):
    queryset.update(status='Upcoming')


def mark_ongoing(modeladmin, request, queryset):
    queryset.update(status='Ongoing')


def mark_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


class OrganizationForm(forms.ModelForm):
    model = Organization

    class Meta:
        fields = ('name', 'type', 'contact', 'num_members', 'notes')

        widgets = {
            'contact': autocomplete.ModelSelect2(url='person-autocomplete'),
        }


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contact', 'num_members', 'notes')
    list_filter = ('type',)
    fields = ('name', 'type', 'contact', 'num_members', 'notes')
    search_fields = ('name', 'type', 'contact__first', 'contact__last', 'num_members', 'notes')
    ordering = ('name',)
    form = OrganizationForm


class ProjectForm(forms.ModelForm):
    model = Project

    class Meta:
        fields = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization', 'community_partner',
                  'notes')
        widgets = {
            'student_partner': autocomplete.ModelSelect2(url='student-autocomplete'),
            'faculty_partner': autocomplete.ModelSelect2(url='faculty-autocomplete'),
            'lafayette_organization': autocomplete.ModelSelect2(url='lafayette-autocomplete'),
            'community_partner': autocomplete.ModelSelect2(url='community-autocomplete')
        }


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization',
                    'community_partner', 'notes')
    list_filter = ('status',)
    search_fields = ('name', 'status', 'student_partner__first', 'student_partner__last', 'faculty_partner__first',
                     'faculty_partner__last', 'lafayette_organization__name',
                     'community_partner__name', 'notes')
    actions = [mark_upcoming, mark_ongoing, mark_completed]
    ordering = ('name',)
    form = ProjectForm


class EventForm(forms.ModelForm):
    model = Event

    class Meta:
        fields = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers', 'notes')

        widgets = {
            'coordinator': autocomplete.ModelSelect2(url='person-autocomplete'),
            'contact': autocomplete.ModelSelect2(url='person-autocomplete'),
            'organization': autocomplete.ModelSelect2(url='organization-autocomplete'),
        }


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers')
    list_filter = ('date', 'pulse_date')
    search_fields = (
        'name', 'coordinator__first', 'coordinator__last', 'contact__first', 'contact__last', 'organization__name',
        'date',
        'pulse_date', 'num_volunteers', 'notes')
    ordering = ('date',)
    form = EventForm


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
