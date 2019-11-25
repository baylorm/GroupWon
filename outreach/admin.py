from django.contrib import admin
from .models import Project, Organization, Event

def mark_upcoming(modeladmin, request, queryset):
    queryset.update(status='Upcoming')
def mark_ongoing(modeladmin, request, queryset):
    queryset.update(status='Ongoing')
def mark_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contact', 'num_members', 'notes')
    list_filter = ('type',)
    fields = ('name', 'type', 'contact', 'num_members', 'notes')
    search_fields = ('name', 'type', 'contact__first', 'contact__last', 'num_members', 'notes')
    ordering = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization',
                    'community_partner', 'notes')
    list_filter = ('status','student_partner', 'faculty_partner', 'lafayette_organization', 'community_partner')
    fields = ('name', 'status', 'student_partner', 'faculty_partner', 'lafayette_organization', 'community_partner',
              'notes')
    search_fields = ('name', 'status', 'student_partner__first', 'student_partner__last', 'faculty_partner__first', 'faculty_partner__last', 'lafayette_organization__name',
                     'community_partner__name', 'notes')
    actions = [mark_upcoming, mark_ongoing, mark_completed]
    ordering = ('name',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers')
    list_filter = ('coordinator', 'organization', 'date', 'pulse_date')
    fields = ('name', 'coordinator', 'contact', 'organization', 'date', 'pulse_date', 'num_volunteers', 'notes')
    search_fields = ('name', 'coordinator__first', 'coordinator__last', 'contact__first', 'contact__last', 'organization__name', 'date', 'pulse_date', 'num_volunteers', 'notes')
    ordering = ('date',)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
