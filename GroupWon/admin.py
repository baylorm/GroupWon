from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User

from outreach.models import Organization, Event, Project
from people.models import Person, FacultyType, Department, Phone


class MyAdminSite(AdminSite):
    site_header = "Landis Center Admin Panel"

admin_site = MyAdminSite(name='landis')
admin_site.register(Phone)
admin_site.register(Person)
admin_site.register(Organization)
admin_site.register(Event)
admin_site.register(Project)
admin_site.register(FacultyType)
admin_site.register(Department)
admin_site.register(Group)
admin_site.register(User)
