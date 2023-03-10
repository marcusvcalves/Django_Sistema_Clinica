from django.contrib import admin
from django.urls import path, include
from .views import home, clientes, agenda, financeiro, cadastrar_usuario, editar_usuario, excluir_usuario, confirmar_exclusao, cadastrar_transacao
from .views import editar_receita, excluir_receita, confirmar_exclusao_receita, editar_despesa, excluir_despesa, confirmar_exclusao_despesa

urlpatterns = [
    path('', home),
    path('clientes', clientes),
    path('agenda', agenda),
    path('financeiro', financeiro),
    path('clientes/', cadastrar_usuario, name="cadastrar_usuario"),
    path('editar/<int:cliente_id>/', editar_usuario, name="editar_usuario"),
    path('excluir/<int:cliente_id>/', excluir_usuario, name="excluir_usuario"),
    path('confirmar/<int:cliente_id>/', confirmar_exclusao, name="confirmar_exclusao"),
    path('financeiro/', cadastrar_transacao, name="cadastrar_transacao"),
    path('editar_receita/<int:receita_id>/', editar_receita, name="editar_receita"),
    path('excluir_receita/<int:receita_id>/', excluir_receita, name="excluir_receita"),
    path('confirmar_exclusao_receita/<int:receita_id>/', confirmar_exclusao_receita, name="confirmar_exclusao_receita"),
    path('editar_despesa/<int:despesa_id>/', editar_despesa, name="editar_despesa"),
    path('excluir_despesa/<int:despesa_id>/', excluir_despesa, name="excluir_despesa"),
    path('confirmar_exclusao_despesa/<int:despesa_id>/', confirmar_exclusao_despesa, name="confirmar_exclusao_despesa"),
]
