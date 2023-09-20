from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page")


def hello(request, username):

    return HttpResponse("<h1>Hello %s</h1>" %username)


def about(request):
    return HttpResponse("About")

def projects(tequest):
    return HttpResponse('projects')


def tasks(tequest):
    return HttpResponse('tasks')

