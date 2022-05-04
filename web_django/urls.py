from django.contrib import admin
from . import views
import apis
from apis import urls
from apis import views as view
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('', views.index),
    path('snake', views.snake),
    path('admin/', admin.site.urls),
    path('apis', include(apis.urls)),
    path('input', views.input_commands),
    path('get_cmd', views.output_commands),
]
