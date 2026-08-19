from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto

@login_required(login_url='login')
def painel(request):
    return render(request, 'painel/painel.html')

# Create your views here.
def cadastro_produto(request):
    return render(request, 'painel/cadastro_produto.html')