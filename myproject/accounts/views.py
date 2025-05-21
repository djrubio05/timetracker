from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/create_user.html"

    def get_success_url(self):
        return reverse("timetracker:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request, "User created and logged in successfully.")
        return response
