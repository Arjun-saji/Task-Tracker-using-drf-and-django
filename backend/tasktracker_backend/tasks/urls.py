from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import TaskDeleteView
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:task_id>/', TaskDeleteView.as_view(), name='task-delete'),
]
