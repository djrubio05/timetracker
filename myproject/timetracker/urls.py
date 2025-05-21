from django.urls import path

from . import views

app_name = "timetracker"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("projects/", views.ProjectsListView.as_view(), name="projects"),
    path("projects/<int:pk>",
         views.ProjectDetailView.as_view(), name="project"),
    path("projects/<int:project_id>/time_entry/<int:pk>/delete",
         views.delete_time_entry, name="delete_time_entry"),
    path("user/<int:pk>/",
         views.UserDetailView.as_view(), name="user"),
]
