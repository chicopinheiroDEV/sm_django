from django.urls import path
from .views import cadastro_produto, contato

urlpatterns = [
    path('cadastro/', cadastro_produto, name='cadastro'),
    path('contato/', contato, name='contato')
]