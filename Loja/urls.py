"""ProjetoLoja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.render_index),
    path('', views.render_nothing),

    path('login/', views.render_login),
    path('login/submit', views.submit_login),
    path('logout_successful/', views.render_logout),
    path('logout/', views.submit_logout),

    path('administrar-produto/', views.render_administrar_produto),
    path('registrar-produto/', views.render_registrar_produto),
    path('registrar-produto/submit', views.submit_registrar_produto),
    path('consultar-produto/', views.render_consultar_produto),
    path('consultar-produto/submit', views.submit_consultar_produto),
    path('alterar-produto/', views.render_alterar_produto),
    path('alterar-produto/submit', views.submit_alterar_produto),
    path('alterar-produto-confirma/', views.render_alterar_produto_confirma),
    path('alterar-produto-confirma/submit', views.submit_alterar_produto_confirma),
    path('excluir-produto/', views.render_excluir_produto),
    path('excluir-produto/submit', views.submit_excluir_produto),
    path('excluir-produto/confirm', views.confirm_excluir_produto),
    path('lista-produtos/', views.render_lista_produtos),

    path('administrar-venda/', views.render_administrar_venda),
    path('registrar-venda/', views.render_registrar_venda),
    path('registrar-venda/submit', views.submit_registrar_venda),
    path('consultar-venda/', views.render_consultar_venda),
    path('consultar-venda/submit', views.submit_consultar_venda),
    path('lista-vendas/', views.render_lista_vendas),
    path('alterar-venda/', views.render_alterar_venda),
    path('excluir-venda/', views.render_excluir_venda),

    path('administrar-vendedor/', views.render_administrar_vendedor),
    path('registrar-vendedor/', views.render_registrar_vendedor),
    path('registrar-vendedor/submit', views.submit_registrar_vendedor),
    path('consultar-vendedor/', views.render_consultar_vendedor),
    path('consultar-vendedor/submit', views.submit_consultar_vendedor),
    path('alterar-vendedor/', views.render_alterar_vendedor),
    path('alterar-vendedor/submit', views.submit_alterar_vendedor),
    path('alterar-vendedor-confirma/', views.render_alterar_vendedor_confirma),
    path('lista-vendedores/', views.render_lista_vendedores),
    path('alterar-vendedor-confirma/submit', views.submit_alterar_vendedor_confirma),
    path('excluir-vendedor/', views.render_excluir_vendedor),
    path('excluir-vendedor/submit', views.submit_excluir_vendedor),
    path('excluir-vendedor/confirm', views.confirm_excluir_vendedor),

    path('administrar-cliente/', views.render_administrar_cliente),
    path('registrar-cliente/', views.render_registrar_cliente),
    path('registrar-cliente/submit', views.submit_registrar_cliente),
    path('consultar-cliente/', views.render_consultar_cliente),
    path('consultar-cliente/submit', views.submit_consultar_cliente),
    path('alterar-cliente/', views.render_alterar_cliente),
    path('alterar-cliente/submit', views.submit_alterar_cliente),
    path('alterar-cliente-confirma/', views.render_alterar_cliente_confirma),
    path('alterar-cliente-confirma/submit', views.submit_alterar_cliente_confirma),
    path('alterar-cliente/confirma', views.submit_alterar_cliente_confirma),
    path('lista-clientes/', views.render_lista_clientes),
    path('excluir-cliente/', views.render_excluir_cliente),
    path('excluir-cliente/submit', views.submit_excluir_cliente),
    path('excluir-cliente/confirm', views.confirm_excluir_cliente),
 
]
