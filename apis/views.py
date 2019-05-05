from django.shortcuts import render
from rest_framework_swagger.views import get_swagger_view
from rest_framework import viewsets
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.response import Response


# Create your views here.
schema_view = get_swagger_view(title='TaskyApp API')

class ProjectViewset(viewsets.ViewSet):
	pass
project_list = ProjectViewset.as_view({'get': 'list'})    	 