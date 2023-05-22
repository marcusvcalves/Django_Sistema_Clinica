from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length = 254, blank=True, null=True, default=None)
    cpf = models.CharField(max_length=100, blank=True, null=True, default=None)
    cep = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    birthDate = models.DateField(blank=True, null=True)
    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        template = ' {0.name}, Telefone: {0.phone}, CPF: {0.cpf}, CEP: {0.cep},  Endereço: {0.address}, Data de Nascimento:{0.birthDate}, Gênero: {0.gender}'
        return template.format(self)

class Cliente(Pessoa):
    ...


class Dentista(Pessoa):
    ...


class Receita(models.Model):
    date = models.DateTimeField(default=timezone.now, editable=True)
    value = models.DecimalField(max_digits=12,decimal_places=2)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    desc = models.CharField(max_length=300, blank=True, null=True)
    pago = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        template = '{0.date}, {0.value}, {0.dentista}, {0.desc},  {0.pago}'
        return template.format(self)

class Despesa(models.Model):
    date = models.DateTimeField(default=timezone.now, editable=True)
    value = models.DecimalField(max_digits=12,decimal_places=2)
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        template = '{0.date}, {0.value}, {0.desc}'
        return template.format(self)

class Event(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    start= models.DateTimeField(null=True,blank=True)
    end= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        template = '{0.id}, {0.cliente}, {0.start}, {0.end}'
        return template.format(self)
    
