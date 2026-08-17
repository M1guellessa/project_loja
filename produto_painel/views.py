from django.shortcuts import render

# Create your views here.
def produto_painel(request):
    return render(request, 'produtos/produtos.html')