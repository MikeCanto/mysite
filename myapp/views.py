from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    return HttpResponse("Index page")


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return HttpResponse("About")


def projects(request):
    projects = list(Project.objects.values_list())
    return JsonResponse(projects, safe=False)


def tasks(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse('task: %s ' % task.title)
