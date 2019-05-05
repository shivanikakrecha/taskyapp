from django.urls import path
from .views import schema_view, ProjectViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'projects', ProjectViewset, basename='project')

urlpatterns = [
    path('apis/v1', schema_view),
    path('apis/v1', ProjectViewset, name="project-list-api")
]