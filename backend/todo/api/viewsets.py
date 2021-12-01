from rest_framework import viewsets

from backend.todo.models import Todo
from backend.todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
