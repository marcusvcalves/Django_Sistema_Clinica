from .models import Cliente, Receita, Despesa, Event
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        if user is None:
            context = {"error": "Usuário ou senha inválidos."}
            return render(request, "login.html", context)
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return render(request, "login.html")


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url='/login')
def home(request):
    return render(request, "index.html")


@login_required(login_url='/login')
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



@login_required(login_url='/login')
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


@login_required(login_url='/login')
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

@login_required(login_url='/login')
def excluir_usuario(request, cliente_id):
    cliente = Cliente.objects.filter(id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect('/clientes')

@login_required(login_url='/login')
def confirmar_exclusao(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "confirmar_exclusao_cliente.html", {'cliente': cliente})

@login_required(login_url='/login')
def dentistas(request):
    return render(request, "dentistas.html")


@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def confirmar_exclusao_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    return render(request, "confirmar_exclusao_receita.html", {'receita': receita})

@login_required(login_url='/login')
def excluir_receita(request, receita_id):
    receita = Receita.objects.filter(id=receita_id)
    receita.delete()
    return HttpResponseRedirect('/financeiro')

@login_required(login_url='/login')
def editar_despesa(request, despesa_id):
    despesa = Despesa.objects.get(id=despesa_id)
    if request.method == 'POST':
        if request.POST.get('valorDespesa'):
            despesa.value = request.POST.get('valorDespesa')
            despesa.desc = request.POST.get('descricaoDespesa')
            despesa.save()

            return HttpResponseRedirect('/financeiro?pg=1')
    return render(request, "editar_despesa.html", {'despesa': despesa})

@login_required(login_url='/login')
def excluir_despesa(request, despesa_id):
    despesa = Despesa.objects.filter(id=despesa_id)
    despesa.delete()
    return HttpResponseRedirect('/financeiro?pg=1')

@login_required(login_url='/login')
def confirmar_exclusao_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)
    return render(request, "confirmar_exclusao_despesa.html", {'despesa': despesa})


@login_required(login_url='/login')
def agenda(request):
    events = Event.objects.all()
    clientes = Cliente.objects.all().order_by('name')
    context = {
        "events": events,
        "clientes": clientes,
    }
    return render(request, "agenda.html", context)


def serialize_cliente(cliente):
    return {
        'id': cliente.id,
        'name': cliente.name,
        'email': cliente.email,
        'cpf': cliente.cpf,
        'cep': cliente.cep,
        'endereco': cliente.address,
        'dataNascimento': cliente.birthDate,
        'genero': cliente.gender,

    }

@login_required(login_url='/login')
def all_events(request):
    all_events = Event.objects.all()
    out = []
    for event in all_events:
        start = timezone.localtime(event.start)
        end = timezone.localtime(event.end)
        cliente_dict = serialize_cliente(event.cliente)
        
        out.append({
            'title': cliente_dict["name"],
            'id': event.id,
            'start': start.strftime('%Y-%m-%d %H:%M:00'),
            'end': end.strftime('%Y-%m-%d %H:%M:00'),
        })
    return JsonResponse(out, safe=False)

@login_required(login_url='/login')
def cadastrar_evento(request):
        if request.method == 'POST':
            event = Event()
            clientID = request.POST.get('eventClient')
            cliente = Cliente.objects.get(id=clientID)
            event.cliente = cliente
            event.start = request.POST.get('eventDate')
            event.end = request.POST.get('eventDate')
            event.save()
            return HttpResponseRedirect('/agenda')

        else:
            return HttpResponseRedirect('/agenda')
        
@login_required(login_url='/login')
def editar_evento(request, event_id):
        event = get_object_or_404(Event, id=event_id)
        clientes = Cliente.objects.all().order_by('name')
        if request.method == 'POST':
            clientID = request.POST.get('eventClient')
            cliente = Cliente.objects.get(id=clientID)
            event.cliente = cliente
            event.start = request.POST.get('eventDate')
            event.end = request.POST.get('eventDate')
            event.save()
            return HttpResponseRedirect('/agenda')

        return render(request, "editar_evento.html", {'event': event, 'clientes': clientes})
        

@login_required(login_url='/login')
def confirmar_exclusao_evento(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "confirmar_exclusao_evento.html", {'event': event})

@login_required(login_url='/login')
def excluir_evento(request, event_id):
    event = Event.objects.filter(id=event_id)
    event.delete()
    return HttpResponseRedirect('/agenda')
