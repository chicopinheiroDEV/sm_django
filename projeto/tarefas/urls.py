from django.urls import path
from .views import get_tarefa

urlpatterns = [
    path('', get_tarefa, name='tarefas')
]
