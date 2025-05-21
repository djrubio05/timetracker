from decimal import Decimal
import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.db.models import Sum
from django.utils import timezone

from .forms import TimeEntryForm, ProjectForm
from .models import Project, TimeEntry


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "timetracker/index.html"


@method_decorator(login_required, name="dispatch")
class ProjectsListView(FormMixin, ListView):
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("timetracker:projects")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.save()
            messages.success(
                self.request, "Project added.")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


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
class UserProjectDetailView(ProjectDetailView):
    template_name = "timetracker/user_project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        '''
            Get target user from url args and
            get all time entry related to target_user
            and current project. Add query result to
            context along with target user.
        '''
        user_id = self.kwargs.get('user_id')
        self.object = self.get_object()

        target_user = User.objects.get(pk=user_id)
        context['target_user'] = target_user

        target_user_time_entries_in_current_project = TimeEntry.objects.filter(
            project=self.object, user=target_user)
        context['user_time_entries'] = target_user_time_entries_in_current_project

        context['total_hours_worked_by_user'] = target_user_time_entries_in_current_project.aggregate(
            total=Sum("worked_hours"))['total'] or Decimal('0.0')

        return context


@method_decorator(login_required, name="dispatch")
class UserWeekDetailView(DetailView):
    model = User
    template_name = "timetracker/user_week_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        '''
            Add past week time entries and total hours
            worked by user in context data to be displayed
            in template.
            
            Re-assign user to request.user as this will be changed
            to target user due to model naming.
        '''

        target_user = self.object
        context['target_user'] = target_user
        context['user'] = self.request.user

        past_week_time = timezone.now() - datetime.timedelta(weeks=1)
        past_week_timeentries = TimeEntry.objects.filter(
            user=target_user.id, created_at__gte=past_week_time)
        context['past_week_time_entries'] = past_week_timeentries

        total_hours_worked_by_user = past_week_timeentries.aggregate(
            total=Sum("worked_hours"))['total'] or Decimal('0.0')
        context['total_hours_worked_by_user'] = total_hours_worked_by_user
        return context


@login_required
def delete_time_entry(request, pk):
    time_entry = get_object_or_404(TimeEntry, pk=pk)
    current_url = request.META.get("HTTP_REFERER")
    if time_entry.user != request.user:
        messages.error(request, "You can only delete your own time entries.")
        return HttpResponseRedirect(current_url)
    if request.method == "POST":
        time_entry.delete()
        messages.success(request, "Task deleted successfully.")
    return HttpResponseRedirect(current_url)
