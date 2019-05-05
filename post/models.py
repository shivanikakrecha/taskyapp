from django.db import models

# Create your models here.


class Post(models.Model):
	post_title = models.CharField(max_length = 100)
	create_at = models.DateField(auto_now_add=True)

	def __str__():
		return self.post_title
