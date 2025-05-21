from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormMixin, DeletionMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from .forms import TimeEntryForm

from .models import Project, TimeEntry


def index(request):
    return HttpResponse("You are at index")


class ProjectsListView(ListView):
    model = Project


class ProjectDetailView(FormMixin, DetailView):
    model = Project
    form_class = TimeEntryForm

    def get_success_url(self):
        return reverse("timetracker:project", args=(self.object.id,))

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


def delete_time_entry(request, project_id, pk):
    task = get_object_or_404(TimeEntry, pk=pk)
    project_id = task.project.id
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
    return HttpResponseRedirect(reverse('timetracker:project', args=(project_id,)))
