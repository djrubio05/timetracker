from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from .forms import TimeEntryForm
from .models import Project, TimeEntry


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "timetracker/index.html"


@method_decorator(login_required, name="dispatch")
class ProjectsListView(ListView):
    model = Project


@method_decorator(login_required, name="dispatch")
class ProjectDetailView(FormMixin, DetailView):
    model = Project
    form_class = TimeEntryForm

    def get_success_url(self):
        return reverse("timetracker:project", args=(self.object.id,))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.project = self.object
            time_entry.user = request.user
            time_entry.save()
            messages.success(
                self.request, "Time Entry added.")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@method_decorator(login_required, name="dispatch")
class UserDetailView(DetailView):
    model = User
    template_name = "timetracker/user_detail.html"


@login_required
def delete_time_entry(request, project_id, pk):
    task = get_object_or_404(TimeEntry, pk=pk)
    project_id = task.project.id
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
    return HttpResponseRedirect(reverse('timetracker:project', args=(project_id,)))
