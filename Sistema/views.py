from .models import Cliente, Receita, Despesa, Events
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.

# @login_required


def home(request):
    return render(request, "index.html")

# @login_required


def agenda(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, "agenda.html", context)

def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        start = timezone.localtime(event.start)
        end = timezone.localtime(event.end)
        
        out.append({
            'title': event.name,
            'id': event.id,
            'start': start.strftime('%Y-%m-%d %H:%M:00'),
            'end': end.strftime('%Y-%m-%d %H:%M:00'),
        })
    return JsonResponse(out, safe=False)

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
        if request.POST.get('clientName'):
            cliente = Cliente()
            cliente.name = request.POST.get('clientName')
            cliente.phone = request.POST.get('clientPhone')
            cliente.email = request.POST.get('clientEmail')
            cliente.cpf = request.POST.get('clientCpf')
            cliente.cep = request.POST.get('clientCep')
            cliente.address = request.POST.get('clientAddress')
            if (request.POST.get('clientBirth') == ""):
                cliente.birthDate = None
            else:
                cliente.birthDate = request.POST.get('clientBirth')
            cliente.gender = request.POST.get('clientGender')
            cliente.save()

            return HttpResponseRedirect('/clientes')

    else:
        return HttpResponseRedirect('/clientes')

# @login_required


def editar_usuario(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        if request.POST.get('clientName'):
            cliente.name = request.POST.get('clientName')
            cliente.phone = request.POST.get('clientPhone')
            cliente.email = request.POST.get('clientEmail')
            cliente.cpf = request.POST.get('clientCpf')
            cliente.cep = request.POST.get('clientCep')
            cliente.address = request.POST.get('clientAddress')
            if (request.POST.get('clientBirth') == ""):
                cliente.birthDate = None
            else:
                cliente.birthDate = request.POST.get('clientBirth')
            cliente.gender = request.POST.get('clientGender')
            cliente.save()
            return HttpResponseRedirect('/clientes')
    return render(request, "editar_cliente.html", {'cliente': cliente})


def excluir_usuario(request, cliente_id):
    cliente = Cliente.objects.filter(id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect('/clientes')


def confirmar_exclusao(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "confirmar_exclusao_cliente.html", {'cliente': cliente})



def financeiro(request):
    pReceita = Paginator(Receita.objects.get_queryset().order_by('id'),10)
    pDespesa = Paginator(Despesa.objects.get_queryset().order_by('id'),10)
    page = request.GET.get('page')
    pg = request.GET.get('pg')
    receita = pReceita.get_page(page)
    despesa = pDespesa.get_page(pg)
    tab_shown = "receita" if page else "despesa" if pg else "receita"

    return render(request, "financeiro.html", {
        "receita": receita,
        "despesa": despesa,
        "tab_shown": tab_shown,
        })


def cadastrar_transacao(request):
    if request.method == 'POST':
        if request.POST.get('valorReceita'):
            receita = Receita()
            receita.value = request.POST.get('valorReceita')
            receita.professional = request.POST.get('profissionalReceita')
            receita.desc = request.POST.get('descricaoReceita')
            pago = request.POST.get('pagoReceita')
            if(pago == "on"):
                receita.pago = True
            else:
                receita.pago = False
            receita.save()
            
            return HttpResponseRedirect('/financeiro')
            
        elif request.POST.get('valorDespesa'):
            despesa = Despesa()
            despesa.value = request.POST.get('valorDespesa')
            despesa.desc = request.POST.get('descricaoDespesa')
            despesa.save()
            
            return HttpResponseRedirect('/financeiro?pg=1')
        else:
            return HttpResponseRedirect('/financeiro')


def editar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    if request.method == 'POST':
        if request.POST.get('valorReceita'):
            receita.value = request.POST.get('valorReceita')
            receita.professional = request.POST.get('profissionalReceita')
            receita.desc = request.POST.get('descricaoReceita')
            pago = request.POST.get('pagoReceita')
            if(pago == "on"):
                receita.pago = True
            else:
                receita.pago = False
            receita.save()

            return HttpResponseRedirect('/financeiro')
    return render(request, "editar_receita.html", {'receita': receita})


def confirmar_exclusao_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    return render(request, "confirmar_exclusao_receita.html", {'receita': receita})

def excluir_receita(request, receita_id):
    receita = Receita.objects.filter(id=receita_id)
    receita.delete()
    return HttpResponseRedirect('/financeiro')


def editar_despesa(request, despesa_id):
    despesa = Despesa.objects.get(id=despesa_id)
    if request.method == 'POST':
        if request.POST.get('valorDespesa'):
            despesa.value = request.POST.get('valorDespesa')
            despesa.desc = request.POST.get('descricaoDespesa')
            despesa.save()

            return HttpResponseRedirect('/financeiro?pg=1')
    return render(request, "editar_despesa.html", {'despesa': despesa})


def confirmar_exclusao_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)
    return render(request, "confirmar_exclusao_despesa.html", {'despesa': despesa})

def excluir_despesa(request, despesa_id):
    despesa = Despesa.objects.filter(id=despesa_id)
    despesa.delete()
    return HttpResponseRedirect('/financeiro?pg=1')

