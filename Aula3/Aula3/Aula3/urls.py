
from django.contrib import admin
from django.urls import path
from .views import produto, categorias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', produto, name='produtos'),
    path('categorias/', categorias, name='categorias')

]
