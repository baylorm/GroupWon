from django.contrib import admin
from .models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'email', 'role')
    fields = ('first', 'last', 'email', 'role',)
    search_fields = ('first', 'last', 'email')


admin.site.register(Person, PersonAdmin)
