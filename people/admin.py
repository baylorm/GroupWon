from django.contrib import admin
from django import forms
from django.utils.html import linebreaks, format_html

from .models import Person, Phone, Department, FacultyType


# Register your models here.

class PhoneInLine(admin.StackedInline):
    model = Phone
    extra = 0
    ordering = ('number',)


class PersonForm(forms.ModelForm):
    model = Person

    class Meta:
        fields = ('first', 'last', 'email', 'role', 'department', 'faculty_type')

    def clean(self):
        faculty_type = self.cleaned_data.get("faculty_type")
        role = self.cleaned_data.get("role")

        if faculty_type and role != "Faculty":
            raise forms.ValidationError("ERROR: The role must be a faculty for the person to have a faculty type")


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last', 'first', 'email', 'role', 'department', 'faculty_type', 'phone_numbers')
    list_filter = ('role', 'faculty_type', 'department')
    search_fields = ('first', 'last', 'email', 'role', 'department__name', 'faculty_type__type')
    inlines = [PhoneInLine]
    form = PersonForm
    ordering = ('last', 'first',)

    def phone_numbers(self, obj):
        number = ""

        for phone in Phone.objects.filter(person=obj):
            if phone != Phone.objects.filter(person=obj).last():
                number += linebreaks(phone.number)
            else:
                number += "<p style=\"display:inline\">" + str(phone.number) + "</p>"

        if number != "":
            return format_html(number)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('type',)
    fields = ('type',)
    search_fields = ('type',)
    ordering = ('type',)


admin.site.register(FacultyType, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Person, PersonAdmin)
