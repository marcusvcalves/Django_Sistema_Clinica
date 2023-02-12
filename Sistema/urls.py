from django.contrib import admin
from django.urls import path, include
from .views import home, pacientes, agenda, financeiro, cadastrar_usuario, editar_usuario, excluir_usuario, confirmar_exclusao

urlpatterns = [
    path('', home),
    path('pacientes', pacientes),
    path('agenda', agenda),
    path('financeiro', financeiro),
    path('pacientes/', cadastrar_usuario, name="cadastrar_usuario"),
    path('editar/<int:paciente_id>/', editar_usuario, name="editar_usuario"),
    path('excluir/<int:paciente_id>/', excluir_usuario, name="excluir_usuario"),
    path('confirmar/<int:paciente_id>/',
         confirmar_exclusao, name="confirmar_exclusao"),
]
