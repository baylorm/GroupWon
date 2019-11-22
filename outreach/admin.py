from django.contrib import admin
from .models import Project, Organization, Event


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contact', 'num_members')
    fields = ('name', 'type', 'contact', 'num_members', 'notes')
    search_fields = ('name', 'type', 'contact', 'num_members', 'notes')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization',
                    'community_partner')
    fields = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization', 'community_partner',
              'notes')
    search_fields = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization',
                     'community_partner', 'notes')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers')
    fields = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers', 'notes')
    search_fields = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers', 'notes')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
