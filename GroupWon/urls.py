"""GroupWon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.views.generic import RedirectView

from GroupWon.views import PersonAutoComplete, StudentAutoComplete, FacultyAutoComplete, LafayetteAutoComplete, \
    CommunityAutoComplete

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),

    url(
        r'^person-autocomplete/$',
        PersonAutoComplete.as_view(),
        name='person-autocomplete',
    ),

    url(
        r'^student-autocomplete/$',
        StudentAutoComplete.as_view(),
        name='student-autocomplete',
    ),

    url(
        r'^faculty-autocomplete/$',
        FacultyAutoComplete.as_view(),
        name='faculty-autocomplete',
    ),

    url(
        r'^lafayette-autocomplete/$',
        LafayetteAutoComplete.as_view(),
        name='lafayette-autocomplete',
    ),

    url(
        r'^community-autocomplete/$',
        CommunityAutoComplete.as_view(),
        name='community-autocomplete',
    ),
]
