from django.urls import include, path
from rest_framework import routers

from backend.todo.views import TodoViewSet

router = routers.DefaultRouter()

router.register(r'todoes', TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
