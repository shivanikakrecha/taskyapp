from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from post.forms import PostForm


# Create your views here.
class PostView(FormView):
	template_name = 'post/post.html'
	form_class = PostForm
