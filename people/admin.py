from django.contrib import admin
from .models import Person, Phone, Department


# Register your models here.

class PhoneInLine(admin.StackedInline):
    model = Phone
    extra = 0
    ordering = ('number',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'email', 'role')
    fields = ('first', 'last', 'email', 'role',)
    search_fields = ('first', 'last', 'email')
    inlines = [PhoneInLine]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'name'
    fields = 'name'
    search_fields = 'name'


admin.site.register(Person, PersonAdmin)
