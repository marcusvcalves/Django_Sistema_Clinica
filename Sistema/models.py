from django.db import models
from cpf_field.models import CPFField


class Paciente(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    cpf = CPFField('cpf')
    cep = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    birthDate = models.DateField(blank=True, null=True)
    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=True, null=True)

    def __str__(self):
        template = '{0.name}, {0.phone}, {0.cpf}, {0.cep},  {0.address}, {0.birthDate}, {0.gender}'
        return template.format(self)


class Receita(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=12,decimal_places=2)
    professional = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=300, blank=True, null=True)
    pago = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        template = '{0.date}, {0.value}, {0.professional}, {0.desc},  {0.pago}'
        return template.format(self)

class Despesa(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=12,decimal_places=2)
    professional = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)

    def __str__(self):
        template = '{0.date}, {0.value}, {0.professional}, {0.desc}'
        return template.format(self)

class Caixa(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=12,decimal_places=3)

    def __str__(self):
        template = '{0.date}, {0.value}, {0.professional}, {0.desc}'
        return template.format(self)