from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index),
    path('apis', include(router.urls)),
    path('input', views.input_commands),
    path('get_cmd', views.output_commands),
    path('api-auth/', include('rest_framework.urls')),
]
