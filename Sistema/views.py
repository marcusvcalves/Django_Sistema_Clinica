from .models import Cliente, Receita, Despesa, Caixa
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


def clientes(request):
    p = Paginator(Cliente.objects.get_queryset().order_by('id'), 10)
    page = request.GET.get('page')
    clientes = p.get_page(page)

    if 'q' in request.GET:
        q = request.GET.get('q')
        clientes = Cliente.objects.all().filter(name__icontains=q)
        context = {
            'clientes' : clientes
            }
        return render(request, "clientes.html", context)
    else:
        return render(request, "clientes.html", {"clientes": clientes})


# @login_required

# @login_required


def cadastrar_usuario(request):
    if request.method == 'POST':
        if request.POST.get('patientName'):
            cliente = Cliente()
            cliente.name = request.POST.get('patientName')
            cliente.phone = request.POST.get('patientPhone')
            cliente.cpf = request.POST.get('patientCpf')
            cliente.cep = request.POST.get('patientCep')
            cliente.address = request.POST.get('patientAddress')
            if (request.POST.get('patientBirth') == ""):
                cliente.birthDate = None
            else:
                cliente.birthDate = request.POST.get('patientBirth')
            cliente.gender = request.POST.get('patientGender')
            cliente.save()

            return HttpResponseRedirect('/clientes')

    else:
        return HttpResponseRedirect('/clientes')

# @login_required


def editar_usuario(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        if request.POST.get('patientName'):
            cliente.name = request.POST.get('patientName')
            cliente.phone = request.POST.get('patientPhone')
            cliente.cpf = request.POST.get('patientCpf')
            cliente.cep = request.POST.get('patientCep')
            cliente.address = request.POST.get('patientAddress')
            if (request.POST.get('patientBirth') == ""):
                cliente.birthDate = None
            else:
                cliente.birthDate = request.POST.get('patientBirth')
            cliente.gender = request.POST.get('patientGender')
            cliente.save()
            return HttpResponseRedirect('/clientes')
    return render(request, "editar.html", {'cliente': cliente})


def excluir_usuario(request, cliente_id):
    cliente = Cliente.objects.filter(id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect('/clientes')


def confirmar_exclusao(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "confirmar.html", {'cliente': cliente})



def financeiro(request):
    pReceita = Paginator(Receita.objects.get_queryset().order_by('id'),10)
    pDespesa = Paginator(Despesa.objects.get_queryset().order_by('id'),5)
    page = request.GET.get('page')
    pg = request.GET.get('pg')
    receita = pReceita.get_page(page)
    despesa = pDespesa.get_page(pg)

    return render(request, "financeiro.html", {
        "receita": receita,
        "despesa": despesa,
        })


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




