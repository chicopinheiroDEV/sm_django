from django.shortcuts import render

def home(request):
    context = {
        'autenticado': True,
        'name' : 'Francisco',
        'idade': 31
    }
    return render (request, 'index.html', context)

def produto(request):
    context = {
        'produtos' : [
            {
                'name': 'Oculus RayBan',
                'descricao': 'Aviador',
                'preco': 1000,
                'estoque': 10
            },
            {
                'name': 'Oculus Chanel',
                'descricao': 'Aviador',
                'preco': 1000,
                'estoque': 20
            },
            {
                'name': 'Oculus Oliver',
                'descricao': 'Aviador',
                'preco': 1000,
                'estoque': 0
            },
            {
                'name': 'Oculus Lentes',
                'descricao': 'Aviador',
                'preco': 1000,
                'estoque': 0
            }
        ]
        
    }
    return render (request, 'index.html', context)