from django.urls import path, include
from rest_framework import routers
from apis.views import schema_view, ProjectViewset, TaskViewset

router = routers.DefaultRouter()
router.register('Projects', ProjectViewset)
router.register('Task', TaskViewset)

urlpatterns = [
    path('', schema_view),
    path('api-path/', include('rest_framework.urls')),
]

urlpatterns += router.urls
