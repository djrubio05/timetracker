from django.urls import path

from . import views

app_name = "timetracker"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.ProjectsListView.as_view(), name="projects"),
    path("projects/<int:pk>",
         views.TimeEntryDetailView.as_view(), name="time_entry"),
]
