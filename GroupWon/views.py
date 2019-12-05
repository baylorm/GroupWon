from dal import autocomplete
from django.db.models import Q

from outreach.models import Organization
from people.models import Person


# Create your views here.
class PersonAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Person.objects.none()

        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(Q(first__icontains=self.q) | Q(last__icontains=self.q))

        return qs


class StudentAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Person.objects.none()

        qs = Person.objects.filter(role="Student")

        if self.q:
            qs = qs.filter(Q(first__icontains=self.q) | Q(last__icontains=self.q))

        return qs


class FacultyAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Person.objects.none()

        qs = Person.objects.filter(role="Faculty")

        if self.q:
            qs = qs.filter(Q(first__icontains=self.q) | Q(last__icontains=self.q))

        return qs


class LafayetteAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Organization.objects.none()

        qs = Organization.objects.filter(Q(type='Club') | Q(type='Course'))

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class CommunityAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Organization.objects.none()

        qs = Organization.objects.filter(type="Community Organization")

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class OrganizationAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Organization.objects.none()

        qs = Organization.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
