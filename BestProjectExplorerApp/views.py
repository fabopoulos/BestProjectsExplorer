# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.measure import D
import json
from django.http import HttpResponse

#from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
#import folium
#import pandas as pd
from django.contrib.gis.geos import GEOSGeometry, Point

from rest_framework import generics, permissions, viewsets
from django.views.generic import TemplateView
from .models import *
from .serializers import *


from django.template.loader import render_to_string


from pyproj import Proj, transform

# TODO faire le ménage

# Create your views here.

# index view : la page index affiche les différents projets. Par un click les projets sont visibles

class ProjectsViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.order_by('best_code')
    serializer_class = ProjectSerializer

#Project
class ProjectCreate(generics.CreateAPIView):
    model = Project
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class ProjectUpdate(generics.UpdateAPIView):
    model = Project
    serializer_class = ProjectSerializer
    lookup_url_kwarg = 'project_pk'
    permission_classes = [permissions.AllowAny]


class ProjectList(generics.ListAPIView):
    model = Project
    queryset = Project.objects.order_by('best_code')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class ProjectDetail(generics.RetrieveAPIView):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_url_kwarg = 'project_pk'
    permission_classes = [permissions.AllowAny]


#Output
class OutputCreate(generics.CreateAPIView):
    model = Output
    serializer_class = OutputSerializer
    permission_classes = [permissions.AllowAny]


class OutputUpdate(generics.UpdateAPIView):
    model = Output

    serializer_class = OutputSerializer
    lookup_url_kwarg = 'output_pk'
    permission_classes = [permissions.AllowAny]


class OutputList(generics.ListCreateAPIView):
    model = Output
    queryset = Output.objects.order_by('name')
    serializer_class = OutputSerializer
    permission_classes = [permissions.AllowAny]


class OutputDetail(generics.RetrieveAPIView):
    model = Output
    queryset = Output.objects.all()
    serializer_class = OutputSerializer
    lookup_url_kwarg = 'output_pk'
    permission_classes = [permissions.AllowAny]


