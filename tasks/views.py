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
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task
from projects.models import Project

# Create your views here.

class TaskCreateView(CreateView):
	"""
	Task create view will create new object in task model. Task form will validate 
	validations of each field by self.If some whorn input will get by widgets than 
	form will raise errors with particuler field.
	"""
	model = Task	
	form_class = TaskForm
	template_name = 'tasks/task_create.html' 

	def get_success_url(self, **kwargs):
		"""
		This method will redirect after saving an object. 
		ex. ('project/4'). Here self.object.project.id will be tagged foreignkey
		for created object.
		"""
		return reverse("project-detail", kwargs={'pk': self.object.project.id })

class TaskEditView(UpdateView):
  model = Task
  fields = ('__all__')
  template_name = 'tasks/task_edit.html'
  context_object_name = 'task'

  def form_valid(self, form):
      post = form.save(commit=False)
      post.save()
      return redirect('project-detail', pk=self.object.project.id)	

class TaskDetailView(DetailView):
	"""
	Task detail view is  developed for project view page. 
	This view will fetch by url order in ('project/2/task/4')
	"""
	model = Task
	template_name = "tasks/task_detail.html"

	def get_context_data(self, **kwargs):
		"""
		This method will return the current task object.
		"""
		context = super().get_context_data(**kwargs)
		context['current_task'] = self.object
		return context

class TaskDeleteView(DeleteView):
	"""
	This method will delete selected object of task.
	"""
	model = Task
	
	def get_success_url(self, **kwargs):
		return reverse("project-detail", kwargs={'pk': self.object.project.id })







