from django.urls import path
from .views import cadastro_tarefa

urlpatterns = [
    path('cadastro/', cadastro_tarefa, name='cadastro')
]