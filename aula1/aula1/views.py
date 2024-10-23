from django.http import HttpResponse, JsonResponse

def saudacao(request):
    return HttpResponse("Olá Usuário")

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

def product(request):
    return HttpResponse(products)