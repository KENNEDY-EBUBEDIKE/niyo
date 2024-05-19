from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import task_list, task_detail


router = DefaultRouter() if settings.DEBUG else SimpleRouter()


app_name = "tasks.api"


urlpatterns = [
    path("", include(router.urls)),
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
]
