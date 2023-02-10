from django.contrib import admin
from django.urls import path, include
from .views import home, pacientes, agenda, financeiro, cadastrar_usuario, editar_usuario

urlpatterns = [
    path('', home),
    path('pacientes', pacientes),
    path('agenda', agenda),
    path('financeiro', financeiro),
    path('pacientes/', cadastrar_usuario, name="cadastrar_usuario"),
    path('editar/<int:paciente_id>/', editar_usuario, name="editar_usuario"),
]
