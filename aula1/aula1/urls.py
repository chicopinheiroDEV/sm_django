from django.contrib import admin
from django.urls import path
from .views import saudacao, personal_data, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saudacao/<str:nome>', saudacao),
    path('personal/', personal_data),
    path('product/<int:id>', product)
    
]
