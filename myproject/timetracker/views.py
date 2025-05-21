from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages

from .forms import TimeEntryForm

from .models import Project, TimeEntry


def index(request):
    return HttpResponse("You are at index")


class ProjectsListView(ListView):
    model = Project


class TimeEntryDetailView(FormMixin, DetailView):
    model = Project
    form_class = TimeEntryForm

    def get_success_url(self):
        return reverse("timetracker:time_entry", args=(self.object.id,))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            task = form.save(commit=False)
            task.project = self.object
            task.save()
            messages.success(
                self.request, "Time Entry added.")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
