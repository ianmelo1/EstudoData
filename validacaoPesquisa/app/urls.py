from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
]
