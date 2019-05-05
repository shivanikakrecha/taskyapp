from django import forms
from .models import Project
from django.contrib.admin import widgets


class ProjectForm(forms.ModelForm):
  
  class Meta:
  	model = Project
  	fields = ('__all__')

