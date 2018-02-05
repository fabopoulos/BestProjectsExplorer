from rest_framework import serializers
from .models import *


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'output_id', 'name', 'target','unit', 'monthly_report')


class OutputSerializer(serializers.ModelSerializer):

    activities = ActivitySerializer(many=True)

    class Meta:
        model = Output
        fields = ('id', 'project_id', 'name', 'activities')


class ProjectSerializer(serializers.ModelSerializer):

    outputs = OutputSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id',
                  'best_code',
                  'grant_type',
                  'name',
                  'organisations',
                  'territory',
                  'start_date',
                  'end_date',
                  'duration',
                  'description',
                  'total_budget',
                  'main_subject',
                  'geom',
                  'outputs')
