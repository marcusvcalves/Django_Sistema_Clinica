from .models import Cliente, Receita, Despesa, Event, Dentista
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
            return render(request, "login/login.html", context)
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return render(request, "login/login.html")


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url='/login')
def home(request):
    return render(request, "home/index.html")


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
        return render(request, "clientes/clientes.html", context)
    else:
        return render(request, "clientes/clientes.html", {"clientes": clientes})



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
    return render(request, "clientes/editar_cliente.html", {'cliente': cliente})

@login_required(login_url='/login')
def excluir_usuario(request, cliente_id):
    cliente = Cliente.objects.filter(id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect('/clientes')

@login_required(login_url='/login')
def confirmar_exclusao(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "clientes/confirmar_exclusao_cliente.html", {'cliente': cliente})

@login_required(login_url='/login')
def dentistas(request):
    p = Paginator(Dentista.objects.get_queryset().order_by('id'), 10)
    page = request.GET.get('page')
    dentistas = p.get_page(page)

    if 'q' in request.GET:
        q = request.GET.get('q')
        dentistas = Dentista.objects.all().filter(name__icontains=q)
        context = {
            'dentistas' : dentistas
            }
        return render(request, "dentistas/dentistas.html", context)
    else:
        return render(request, "dentistas/dentistas.html", {"dentistas": dentistas})

@login_required(login_url='/login')
def cadastrar_dentista(request):
    if request.method == 'POST':
        if request.POST.get('dentistName'):
            dentista = Dentista()
            dentista.name = request.POST.get('dentistName')
            dentista.phone = request.POST.get('dentistPhone')
            dentista.email = request.POST.get('dentistEmail')
            dentista.cpf = request.POST.get('dentistCpf')
            dentista.cep = request.POST.get('dentistCep')
            dentista.address = request.POST.get('dentistAddress')
            if (request.POST.get('dentistBirth') == ""):
                dentista.birthDate = None
            else:
                dentista.birthDate = request.POST.get('dentistBirth')
            dentista.gender = request.POST.get('dentistGender')
            dentista.save()

            return HttpResponseRedirect('/dentistas')

    else:
        return HttpResponseRedirect('/dentistas')


@login_required(login_url='/login')
def editar_dentista(request, dentista_id):
    dentista = Dentista.objects.get(id=dentista_id)
    if request.method == 'POST':
        if request.POST.get('clientName'):
            dentista.name = request.POST.get('clientName')
            dentista.phone = request.POST.get('clientPhone')
            dentista.email = request.POST.get('clientEmail')
            dentista.cpf = request.POST.get('clientCpf')
            dentista.cep = request.POST.get('clientCep')
            dentista.address = request.POST.get('clientAddress')
            if (request.POST.get('clientBirth') == ""):
                dentista.birthDate = None
            else:
                dentista.birthDate = request.POST.get('clientBirth')
            dentista.gender = request.POST.get('clientGender')
            dentista.save()
            return HttpResponseRedirect('/clientes')
    return render(request, "dentistas/editar_dentista.html", {'dentista': dentista})

@login_required(login_url='/login')
def excluir_dentista(request, dentista_id):
    dentista = Dentista.objects.filter(id=dentista_id)
    dentista.delete()
    return HttpResponseRedirect('/dentistas')

@login_required(login_url='/login')
def confirmar_exclusao_dentista(request, dentista_id):
    dentista = get_object_or_404(Dentista, id=dentista_id)
    return render(request, "dentistas/confirmar_exclusao_dentista.html", {'dentista': dentista})


@login_required(login_url='/login')
def financeiro(request):
    pReceita = Paginator(Receita.objects.get_queryset().order_by('id'),10)
    pDespesa = Paginator(Despesa.objects.get_queryset().order_by('id'),10)
    dentistas = Dentista.objects.all().order_by('name')
    page = request.GET.get('page')
    pg = request.GET.get('pg')
    receita = pReceita.get_page(page)
    despesa = pDespesa.get_page(pg)
    tab_shown = "receita" if page else "despesa" if pg else "receita"
    context = {
        "receita": receita,
        "despesa": despesa,
        "tab_shown": tab_shown,
        "dentistas": dentistas
    }

    return render(request, "financeiro/financeiro.html", context)

@login_required(login_url='/login')
def cadastrar_transacao(request):
    if request.method == 'POST':
        if request.POST.get('valorReceita'):
            receita = Receita()
            receita.value = request.POST.get('valorReceita')
            dentistID = request.POST.get('dentistaReceita')
            dentista = Dentista.objects.get(id=dentistID)
            receita.dentista = dentista
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
    dentistas = Dentista.objects.all().order_by('name')
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
    context = {
        'receita': receita,
        'dentistas': dentistas
    }
    return render(request, "financeiro/editar_receita.html", context)

@login_required(login_url='/login')
def confirmar_exclusao_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    return render(request, "financeiro/confirmar_exclusao_receita.html", {'receita': receita})

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
    return render(request, "financeiro/editar_despesa.html", {'despesa': despesa})

@login_required(login_url='/login')
def excluir_despesa(request, despesa_id):
    despesa = Despesa.objects.filter(id=despesa_id)
    despesa.delete()
    return HttpResponseRedirect('/financeiro?pg=1')

@login_required(login_url='/login')
def confirmar_exclusao_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)
    return render(request, "financeiro/confirmar_exclusao_despesa.html", {'despesa': despesa})


@login_required(login_url='/login')
def agenda(request):
    events = Event.objects.all()
    clientes = Cliente.objects.all().order_by('name')
    dentistas = Dentista.objects.all().order_by('name')
    context = {
        "events": events,
        "clientes": clientes,
        "dentistas": dentistas
    }
    return render(request, "agenda/agenda.html", context)


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
            dentistID = request.POST.get('eventDentist')
            dentista = Dentista.objects.get(id=dentistID)
            event.dentista = dentista
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
        dentista = Dentista.objects.all().order_by('name')
        context = {
        "event": event,
        "clientes": clientes,
        "dentistas": dentista
        }

        if request.method == 'POST':
            clientID = request.POST.get('eventClient')
            cliente = Cliente.objects.get(id=clientID)
            event.cliente = cliente
            event.start = request.POST.get('eventDate')
            event.end = request.POST.get('eventDate')
            event.save()
            return HttpResponseRedirect('/agenda')

        return render(request, "agenda/editar_evento.html", context)
        

@login_required(login_url='/login')
def confirmar_exclusao_evento(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "agenda/confirmar_exclusao_evento.html", {'event': event})

@login_required(login_url='/login')
def excluir_evento(request, event_id):
    event = Event.objects.filter(id=event_id)
    event.delete()
    return HttpResponseRedirect('/agenda')
