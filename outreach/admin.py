from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    fields = ('name', 'status', 'notes',)
    search_fields = ('name', 'status', 'notes')


admin.site.register(Project, ProjectAdmin)