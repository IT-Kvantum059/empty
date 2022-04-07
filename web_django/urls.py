from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('input', views.input_commands),
    path('get_cmd', views.output_commands)
]
