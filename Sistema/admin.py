from django.contrib import admin
from .models import Cliente, Receita, Despesa, Caixa, Events, Dentista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Caixa)
admin.site.register(Events)
admin.site.register(Dentista)
