from django.contrib import admin
from .models import Person, Phone, Department, FacultyType


# Register your models here.

class PhoneInLine(admin.StackedInline):
    model = Phone
    extra = 0
    ordering = ('number',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    fields = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    search_fields = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    inlines = [PhoneInLine]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('type',)
    fields = ('type',)
    search_fields = ('type',)


admin.site.register(FacultyType, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Person, PersonAdmin)
