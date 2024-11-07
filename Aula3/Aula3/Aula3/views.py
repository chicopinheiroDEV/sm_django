from django.shortcuts import render


def produto(request):
    context = {
        'produtos': [
            {
                'name': 'Produto1',
                'price': 50,
                'category': 'Eletrônico'
            },
            {
                'name': 'Produto2',
                'price': 70,
                'category': 'Eletrônico'
            }
        ]
    }
    return render(request, 'produtos.html', context)

def categorias(request):
    context = {
        'categorias': [
            'Eletrônicos',
            'Bebidas Alcoólicas'
        ]
    }

    return render (request, 'categoria.html', context)