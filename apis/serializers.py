from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from tasks.models import Task
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'