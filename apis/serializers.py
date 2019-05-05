from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from tasks.models import Task
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
	model = Project
	fields = ('__all__')

class TaskSerializer(serializers.ModelSerializer):
	model = Task
	fields = ('__all__')