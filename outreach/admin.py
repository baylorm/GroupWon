from django.contrib import admin
from .models import Project, Organization


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'num_members')
    fields = ('name', 'type', 'num_members', 'notes', 'contact')
    search_fields = ('name', 'type', 'num_members', 'notes')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'community_partner', 'lafayette_organization')
    fields = ('name', 'status', 'notes', 'community_partner', 'lafayette_organization', 'student_partner',
              'faculty_partner')
    search_fields = ('name', 'status', 'notes', 'community_partner', 'lafayette_organization')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'pulse_date', 'num_volunteers')
    fields = ('name', 'date', 'pulse_date', 'num_volunteers', 'notes', 'coordinator', 'contact', 'organization')
    search_fields = ('name', 'date', 'pulse_date', 'num_volunteers', 'notes')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
