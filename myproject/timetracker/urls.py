from django.urls import path

from . import views

app_name = "timetracker"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:project_id>", views.tasks, name="tasks"),
]
