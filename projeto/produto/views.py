from django.shortcuts import render
from .models import Produto

# Create your views here.
def get_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    
    return render(request, 'produtos.html', context) 