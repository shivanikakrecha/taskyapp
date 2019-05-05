from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import UpdateView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ProjectForm
from .models import Project
from tasks.models import Task

# Create your views here.

class ProjectListView(ListView):
	model = Project
	context_object_name = 'projects'
	template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
	model = Task
	template_name = "projects/project_detail.html"

	def get_object(self):
		project = get_object_or_404(Project, pk=self.kwargs['pk'])
		print(self.model.objects.filter(pk=self.kwargs['pk']))
		return self.model.objects.filter(pk=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		context['tasks'] = Task.objects.filter(project__id=self.kwargs['pk'])
		return context

class ProjectCreateView(CreateView):
	model = Project	
	form_class = ProjectForm
	template_name = 'projects/project_create.html'
	success_url = "/projects/"

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
	model = Project
	success_url = "/projects/"







