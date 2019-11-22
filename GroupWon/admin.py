from django.contrib.admin import AdminSite
from people.models import Person


class MyAdminSite(AdminSite):
    site_header = "Landis Center Admin Panel"


admin_site = MyAdminSite(name='landis')
admin_site.register(Person)