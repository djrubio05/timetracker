from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, TimeEntry


def index(request):
    return HttpResponse("You are at index")


class ProjectsListView(ListView):
    model = Project


class TimeEntryDetailView(DetailView):
    model = Project
