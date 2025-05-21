from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("You are at index")


def projects(request):
    return HttpResponse("You are at projects")


def tasks(request, project_id):
    return HttpResponse(f"You are at tasks for project:{project_id}")
