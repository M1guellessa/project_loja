from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto

@login_required(login_url='login')
def painel(request):
    produtos = Produto.objects.all()
    return render(request, 'painel/painel.html')

# Create your views here.
def cadastro_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        produto.save()

    return render(request, 'painel/cadastro_produto.html')