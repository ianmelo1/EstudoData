from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']

def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})