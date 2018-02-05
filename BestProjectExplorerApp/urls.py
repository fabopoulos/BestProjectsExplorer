from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import ProjectsViewSet,ProjectList, OutputList, ProjectDetail, ProjectUpdate, OutputDetail, OutputUpdate

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Projects', ProjectsViewSet)

urlpatterns = [
    url(r'^projects$', ProjectList.as_view(), name='projects_list'),
    url(r'^projects/(?P<project_pk>[0-9]+)$', ProjectDetail.as_view(), name='project_detail'),
    url(r'^projects/update/(?P<project_pk>[0-9]+)$', ProjectUpdate.as_view(), name='project_update'),

    url(r'^outputs$', OutputList.as_view(), name='outputs_list'),
    url(r'^outputs/(?P<output_pk>[0-9]+)$', OutputDetail.as_view(), name='output_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
