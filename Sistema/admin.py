from django.contrib import admin
from .models import Paciente, Receita, Despesa, Caixa

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Caixa)
