from django.urls import path
from .views import get_produtos

urlpatterns = [
    path('', get_produtos, name='produtos')
]
 