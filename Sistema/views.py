from django.shortcuts import render
from .models import Paciente
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, "index.html")


def agenda(request):
    return render(request, "agenda.html")


def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes.html", {"pacientes": pacientes})


def financeiro(request):
    return render(request, "financeiro.html")


def cadastrar_usuario(request):
    if request.method == 'POST':
        if request.POST.get('patientName'):
            paciente = Paciente()
            paciente.name = request.POST.get('patientName')
            paciente.phone = request.POST.get('patientPhone')
            paciente.cpf = request.POST.get('patientCpf')
            paciente.cep = request.POST.get('patientCep')
            paciente.address = request.POST.get('patientAddress')
            paciente.dateOfBirth = request.POST.get('patientBirth')
            paciente.gender = request.POST.get('patientGender')
            paciente.save()

            return HttpResponseRedirect('/pacientes')

    else:
        return HttpResponseRedirect('/pacientes')
