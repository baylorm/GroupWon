from django.contrib import admin
from .models import Person
from .models import Department
from .models import Phone
from .models import FacultyType


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'email', 'role')
    fields = ('first', 'last', 'email', 'role',)
    search_fields = ('first', 'last', 'email')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('number',)
    fields = ('number',)
    search_fields = ('number',)


class FacultyTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    fields = ('type',)
    search_fields = ('type',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(FacultyType, FacultyTypeAdmin)
