# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dp'
urlpatterns = [
    url(
        regex="^Some/~create/$",
        view=views.SomeCreateView.as_view(),
        name='Some_create',
    ),
    url(
        regex="^Some/(?P<pk>\d+)/~delete/$",
        view=views.SomeDeleteView.as_view(),
        name='Some_delete',
    ),
    url(
        regex="^Some/(?P<pk>\d+)/$",
        view=views.SomeDetailView.as_view(),
        name='Some_detail',
    ),
    url(
        regex="^Some/(?P<pk>\d+)/~update/$",
        view=views.SomeUpdateView.as_view(),
        name='Some_update',
    ),
    url(
        regex="^Some/$",
        view=views.SomeListView.as_view(),
        name='Some_list',
    ),
	url(
        regex="^Thing/~create/$",
        view=views.ThingCreateView.as_view(),
        name='Thing_create',
    ),
    url(
        regex="^Thing/(?P<pk>\d+)/~delete/$",
        view=views.ThingDeleteView.as_view(),
        name='Thing_delete',
    ),
    url(
        regex="^Thing/(?P<pk>\d+)/$",
        view=views.ThingDetailView.as_view(),
        name='Thing_detail',
    ),
    url(
        regex="^Thing/(?P<pk>\d+)/~update/$",
        view=views.ThingUpdateView.as_view(),
        name='Thing_update',
    ),
    url(
        regex="^Thing/$",
        view=views.ThingListView.as_view(),
        name='Thing_list',
    ),
	]
