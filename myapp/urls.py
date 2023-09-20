from django.urls import path
from . import views

# SECONDARY URLS

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/<str:title>', views.tasks),

]

# ME QUEDE EN EL MINUTO 1:38:13