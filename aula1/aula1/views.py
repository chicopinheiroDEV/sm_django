from django.http import HttpResponse, JsonResponse

def saudacao(request, nome):
    return HttpResponse(f'Olá {nome}! Seu nome tem {len(nome)} caracteres ')

def personal_data(request):
    return JsonResponse({
        "nome": "Francisco",
        "e-mail": "qualquercoisa@gmail.com"
    })
 
    
products = [
    {
        'id': 1,
        'name': 'pao',
        'price': 0.50,
        'stock': 100
    },
    {
        'id': 2,
        'name': 'queijo',
        'price': 10,
        'stock': 20
    }
]

def product(request, id):
    for product in products:
        if product['id'] == id:
                return JsonResponse(product)