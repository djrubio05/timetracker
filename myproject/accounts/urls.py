
from django.urls import path, include
from django.contrib.auth import views as authviews
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", authviews.LoginView.as_view(), name="login"),
    path("logout/", authviews.LogoutView.as_view(), name="logout"),
    path("register/", views.UserCreateView.as_view(), name="register"),
]
