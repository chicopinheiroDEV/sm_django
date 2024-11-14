from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produto.urls')),
    path('tarefas/', include('tarefas.urls'))
]
