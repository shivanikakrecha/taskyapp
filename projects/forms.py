from django import forms
from .models import Project
from django.contrib.admin import widgets


class ProjectForm(forms.ModelForm):
  class Meta:
  	model = Project
  	fields = ('__all__')
  	widgets = {
          'description': forms.Textarea(attrs={'rows':70, 'cols':40}),
        }

  def __init__(self, *args, **kwargs):
  	super(ProjectForm, self).__init__(*args, **kwargs)
  	self.fields['duration'].widget = widgets.AdminDateWidget()

