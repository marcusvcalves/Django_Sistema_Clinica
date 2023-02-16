from .models import Paciente, Receita, Despesa, Caixa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator


# Create your views here.

# @login_required


def home(request):
    return render(request, "index.html")

# @login_required


def agenda(request):
    return render(request, "agenda.html")

# @login_required


def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes.html", {"pacientes": pacientes})


# @login_required


    #despesa = get_object_or_404(Despesa, id=despesa_id)
    #caixa = get_object_or_404(Caixa, id=caixa_id)
    #return render(request, "financeiro.html", {'receita': receita}, {'despesa': despesa}, {'caixa': caixa})

# @login_required


def cadastrar_usuario(request):
    if request.method == 'POST':
        if request.POST.get('patientName'):
            paciente = Paciente()
            paciente.name = request.POST.get('patientName')
            paciente.phone = request.POST.get('patientPhone')
            paciente.cpf = request.POST.get('patientCpf')
            paciente.cep = request.POST.get('patientCep')
            paciente.address = request.POST.get('patientAddress')
            if (request.POST.get('patientBirth') == ""):
                paciente.birthDate = None
            else:
                paciente.birthDate = request.POST.get('patientBirth')
            paciente.gender = request.POST.get('patientGender')
            paciente.save()

            return HttpResponseRedirect('/pacientes')

    else:
        return HttpResponseRedirect('/pacientes')

# @login_required


def editar_usuario(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == 'POST':
        if request.POST.get('patientName'):
            paciente.name = request.POST.get('patientName')
            paciente.phone = request.POST.get('patientPhone')
            paciente.cpf = request.POST.get('patientCpf')
            paciente.cep = request.POST.get('patientCep')
            paciente.address = request.POST.get('patientAddress')
            if (request.POST.get('patientBirth') == ""):
                paciente.birthDate = None
            else:
                paciente.birthDate = request.POST.get('patientBirth')
            paciente.gender = request.POST.get('patientGender')
            paciente.save()
            return HttpResponseRedirect('/pacientes')
    return render(request, "editar.html", {'paciente': paciente})


def excluir_usuario(request, paciente_id):
    paciente = Paciente.objects.filter(id=paciente_id)
    paciente.delete()
    return HttpResponseRedirect('/pacientes')


def confirmar_exclusao(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, "confirmar.html", {'paciente': paciente})



def financeiro(request):
    receita = Receita.objects.all()
    despesa = Despesa.objects.all()
    return render(request, "financeiro.html", {"receita": receita, "despesa": despesa})

def cadastrar_transacao(request):
    if request.method == 'POST':
        if request.POST.get('valorReceita'):
            receita = Receita()
            receita.value = request.POST.get('valorReceita')
            receita.professional = request.POST.get('profissionalReceita')
            receita.desc = request.POST.get('descricaoReceita')
            receita.pago = request.POST.get('pagoReceita')
            receita.save()
            
            return HttpResponseRedirect('/financeiro')
            
        elif request.POST.get('valorDespesa'):
            despesa = Despesa()
            despesa.value = request.POST.get('valorDespesa')
            despesa.desc = request.POST.get('descricaoDespesa')
            despesa.save()
            
            return HttpResponseRedirect('/financeiro')
        else:
            return HttpResponseRedirect('/financeiro')




