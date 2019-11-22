from django.contrib import admin
from .models import Person, Phone, Department, FacultyType


# Register your models here.

class PhoneInLine(admin.StackedInline):
    model = Phone
    extra = 0
    ordering = ('number',)


class FacultyTypeInLine(admin.StackedInline):
    model = FacultyType
    extra = 0
    ordering = ('type',)


# class FacultyTypeAdmin(admin.ModelAdmin):
#     list_display = 'type'
#     fields = 'type'
#     search_fields = 'type'


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    fields = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    search_fields = ('first', 'last', 'email', 'role', 'department', 'faculty_type')
    inlines = [PhoneInLine, FacultyTypeInLine]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'name'
    fields = 'name'
    search_fields = 'name'


admin.site.register(Person, PersonAdmin)
