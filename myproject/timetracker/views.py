from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import TimeEntryForm

from .models import Project, TimeEntry


def index(request):
    return HttpResponse("You are at index")


class ProjectsListView(ListView):
    model = Project


class TimeEntryDetailView(FormMixin, DetailView):
    model = Project
    form_class = TimeEntryForm
