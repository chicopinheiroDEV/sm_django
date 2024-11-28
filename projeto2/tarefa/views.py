from django.shortcuts import render
from .forms import TarefaForm



def cadastro_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            form = TarefaForm()
    else:
        form = TarefaForm()
    return render (request, 'tarefa.html', {'form': form})
