from django.contrib import admin
from .models import Cliente, Receita, Despesa, Event, Dentista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Event)
admin.site.register(Dentista)
