from django.shortcuts import render
from .forms import ContatoForm, ProdutoForm

#Formulário com conexão no banco de dados
def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()
    return render (request, 'cadastro.html', {'form': form})


# Formulário sem conexão com o banco de dados
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        print(form)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

    else: 
        form = ContatoForm()
    return render(request, 'formulario.html', {'form': form})