from django.contrib import admin
from django.urls import path, include
from .views import home, clientes, agenda, financeiro, cadastrar_usuario, editar_usuario, excluir_usuario, confirmar_exclusao, cadastrar_transacao

urlpatterns = [
    path('', home),
    path('clientes', clientes),
    path('agenda', agenda),
    path('financeiro', financeiro),
    path('clientes/', cadastrar_usuario, name="cadastrar_usuario"),
    path('editar/<int:cliente_id>/', editar_usuario, name="editar_usuario"),
    path('excluir/<int:cliente_id>/', excluir_usuario, name="excluir_usuario"),
    path('confirmar/<int:cliente_id>/',
         confirmar_exclusao, name="confirmar_exclusao"),
    path('financeiro/', cadastrar_transacao, name="cadastrar_transacao"),
]
