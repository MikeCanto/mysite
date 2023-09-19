from django.urls import path
from . import views

# SECONDARY URLS

urlpatterns = [
    path('', views.hello),
    path('about/', views.about)

]