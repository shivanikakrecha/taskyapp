from django.urls import path
from .views import TaskCreateView, TaskEditView, TaskDetailView, TaskDeleteView

urlpatterns = [
    path('<int:project_pk>/task-create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:project_pk>/task-edit/<int:pk>/', TaskEditView.as_view(), name='task-edit'),
    path('<int:project_pk>/task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),	
    path('<int:project_pk>/task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]