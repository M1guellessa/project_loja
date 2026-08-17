"""
URL configuration for lolja_pj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lolja_app import views as lolja_views
from carrinho_app import views as carrinho_views
from login import views as login_views
from cadastro import views as cadastro_views
from painel import views as painel_views
from produto_painel import views as produto_painel_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', lolja_views.home, name='home'),
    path('', lolja_views.home, name='home'),
    path('carrinho/', carrinho_views.carrinho, name='carrinho'),
    path('login/', login_views.login_views, name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('painel/', painel_views.painel, name='painel'),
    path('cadastro/', cadastro_views.cadastro, name='cadastro'),
    path('produto_painel/', produto_painel_views.produto_painel, name='produto_painel'),
]
