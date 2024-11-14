from django.shortcuts import render
from .models import Tarefas

# Create your views here.
def get_tarefa(request):
    tarefas = Tarefas.objects.all()
    context = {
        'tarefas': tarefas
    }
    
    return render (request, 'tarefas.html', context)