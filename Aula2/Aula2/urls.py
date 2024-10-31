from django.contrib import admin
from django.urls import path
from .views import home, produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('produto/', produto)
]
