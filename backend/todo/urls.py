from django.urls import include, path
from rest_framework import routers

from backend.todo.api.viewsets import TodoViewSet

app_name = 'todo'

router = routers.DefaultRouter()

router.register(r'todos', TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
