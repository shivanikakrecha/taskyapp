from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectEditView, ProjectDeleteView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list' ),
    path('create/', ProjectCreateView.as_view(), name='project-create' ),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project-edit/<int:pk>/', ProjectEditView.as_view(), name='project-edit'),
    path('project-delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
]