from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, TimeEntry


def index(request):
    return HttpResponse("You are at index")


def tasks(request, project_id):
    return HttpResponse(f"You are at tasks for project:{project_id}")


class ProjectsListView(ListView):
    model = Project


class TimeEntryDetailView(DetailView):
    model = Project
