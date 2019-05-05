from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=50, verbose_name="name")
	description = models.TextField()
	duration = models.DateTimeField()
	avtar = models.ImageField(upload_to='Project_avtar', null=True, blank=True)

	def  __str__(self):
		return self.name