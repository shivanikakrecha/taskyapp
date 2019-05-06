from django.shortcuts import render
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView, 
	ListView, 
	DetailView
)
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ProjectForm
from .models import Project
from tasks.models import Task

# Create your views here.

class ProjectListView(ListView):
	"""
	This view is created for display project list from Project midel all objects. 
	"""
	model = Project
	context_object_name = 'projects'
	template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
	"""
	Project detail view will display all the task list into each project.
	ex. Project1 have 5 tasks, according to this it will show something in 
	url like ( project/5/) 
	"""
	model = Task
	template_name = "projects/project_detail.html"

	def get_object(self):
		"""
		This method will fetch current project object according to url. 
		"""
		project = get_object_or_404(Project, pk=self.kwargs['pk'])
		print(self.model.objects.filter(pk=self.kwargs['pk']))
		return project

	def get_context_data(self, **kwargs):
		"""
		This method is use for context data which is used by its template 
		"projects/project_detail.html"
		"""
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		context['tasks'] = Task.objects.filter(project__id=self.kwargs['pk'])
		context['project'] = self.get_object()
		return context

class ProjectCreateView(CreateView):
	"""
	Project createview will create new object of Project model. Projectfrom will
	managed all validations by it self. 
	"""
	model = Project	
	form_class = ProjectForm
	template_name = 'projects/project_create.html'
	success_url = "/"

class ProjectEditView(UpdateView):
  model = Project
  fields = ('__all__')
  template_name = 'projects/project_edit.html'
  context_object_name = 'project' 

  def form_valid(self, form):
      post = form.save(commit=False)
      post.save()
      return redirect('project-list')

class ProjectDeleteView(DeleteView):
	"""
	Project delete view will delete the selected object. It will fetch deleted object 
	id from url it self. 	
	"""
	model = Project
	success_url = reverse_lazy('project-list')







