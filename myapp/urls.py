from django.urls import path
from . import views

# SECONDARY URLS

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),

]

# ME QUEDE EN EL MINUTO 1:29:41