from django.db import models
from django.apps import apps
from projects.models import Project



# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=50, verbose_name="name")
	description = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField(auto_now=False, auto_now_add=False)
	project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True, auto_now=False)
	updated_at = models.DateField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name
