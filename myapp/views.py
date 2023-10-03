from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    title = 'Django course!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'Mike'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values_list())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects

    })


def tasks(request):
    # task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
