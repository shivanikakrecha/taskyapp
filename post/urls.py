from django.urls import path
from django.views.generic import TemplateView
from post.views import PostView

urlpatterns = [
    path('', PostView.as_view() , name="add-post") 
]