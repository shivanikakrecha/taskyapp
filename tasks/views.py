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
	model = Task	
	form_class = TaskForm
	template_name = 'tasks/task_create.html' 

	def get_success_url(self, **kwargs):
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
	model = Task
	template_name = "tasks/task_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['current_task'] = self.object
		return context

class TaskDeleteView(DeleteView):
	model = Task
	
	def get_success_url(self, **kwargs):
		return reverse("project-detail", kwargs={'pk': self.object.project.id })







