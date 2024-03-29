from django.contrib import admin
from django.urls import path, include
from .views import home, clientes, agenda, financeiro, cadastrar_usuario, editar_usuario, excluir_usuario, confirmar_exclusao, cadastrar_transacao
from .views import editar_receita, excluir_receita, confirmar_exclusao_receita, editar_despesa, excluir_despesa, confirmar_exclusao_despesa, all_events, login_view, logout_view
from .views import cadastrar_evento, dentistas, editar_evento, confirmar_exclusao_evento, excluir_evento, cadastrar_dentista, editar_dentista, excluir_dentista, confirmar_exclusao_dentista

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('', home, name="home"),
    path('clientes', clientes, name="clientes"),
    path('clientes/', cadastrar_usuario, name="cadastrar_usuario"),
    path('editar/<int:cliente_id>/', editar_usuario, name="editar_usuario"),
    path('excluir/<int:cliente_id>/', excluir_usuario, name="excluir_usuario"),
    path('confirmar/<int:cliente_id>/', confirmar_exclusao, name="confirmar_exclusao"),
    path('dentistas', dentistas, name="dentistas"),
    path('dentistas/', cadastrar_dentista, name="cadastrar_dentista"),
    path('editar_dentista/<int:dentista_id>/', editar_dentista, name="editar_dentista"),
    path('excluir_dentista/<int:dentista_id>/', excluir_dentista, name="excluir_dentista"),
    path('confirmar_exclusao_dentista/<int:dentista_id>/', confirmar_exclusao_dentista, name="confirmar_exclusao_dentista"),
    path('financeiro', financeiro, name="financeiro"),
    path('financeiro/', cadastrar_transacao, name="cadastrar_transacao"),
    path('editar_receita/<int:receita_id>/', editar_receita, name="editar_receita"),
    path('excluir_receita/<int:receita_id>/', excluir_receita, name="excluir_receita"),
    path('confirmar_exclusao_receita/<int:receita_id>/', confirmar_exclusao_receita, name="confirmar_exclusao_receita"),
    path('editar_despesa/<int:despesa_id>/', editar_despesa, name="editar_despesa"),
    path('excluir_despesa/<int:despesa_id>/', excluir_despesa, name="excluir_despesa"),
    path('confirmar_exclusao_despesa/<int:despesa_id>/', confirmar_exclusao_despesa, name="confirmar_exclusao_despesa"),
    path('agenda', agenda, name="agenda"),
    path('all_events', all_events, name="all_events"),
    path('agenda/', cadastrar_evento, name="cadastrar_evento"),
    path('editar_evento/<int:event_id>', editar_evento, name="editar_evento"),
    path('confirmar_exclusao_evento/<int:event_id>/', confirmar_exclusao_evento, name="confirmar_exclusao_evento"),
    path('excluir_evento/<int:event_id>/', excluir_evento, name="excluir_evento"),
]
