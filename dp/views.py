# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Some,
	Thing,
)


class SomeCreateView(CreateView):

    model = Some


class SomeDeleteView(DeleteView):

    model = Some


class SomeDetailView(DetailView):

    model = Some


class SomeUpdateView(UpdateView):

    model = Some


class SomeListView(ListView):

    model = Some


class ThingCreateView(CreateView):

    model = Thing


class ThingDeleteView(DeleteView):

    model = Thing


class ThingDetailView(DetailView):

    model = Thing


class ThingUpdateView(UpdateView):

    model = Thing


class ThingListView(ListView):

    model = Thing

