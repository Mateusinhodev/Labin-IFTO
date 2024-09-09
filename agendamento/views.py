from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Agendamentos, Laboratorios, Professores
from .forms import AgendamentoAula
from .serializers import AgendamentoSerializer
from rest_framework import viewsets

# É onde encontra se toda a lógica do sistema.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        agendamentos = Agendamentos.objects.all()
        form = AgendamentoAula()

        return render(request, 'home.html', {'agendamentos': agendamentos,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form})
    else: 
        return redirect('/auth/login/?status=2')
    
def ver_agendamento(request, id):
    if request.session.get('usuario'):
        agendamento = Agendamentos.objects.get(id = id)
        laboratorio = Laboratorios.objects.all()
        professor = Professores.objects.all()
        form = AgendamentoAula()

        return render(request, 'ver_agendamento.html', {'agendamento': agendamento,
                                                        'laboratorio': laboratorio,
                                                        'professor': professor,
                                                        'usuario_logado': request.session.get('usuario'),
                                                        'form': form})
    return redirect('/auth/login/?status=2')

def agendamento_aula(request):
    if request.method == 'POST':
        form = AgendamentoAula(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/agendamento/home')
        else:
            return HttpResponse('Dados Inválidos')
        # laboratorio = form.data['laboratorio']
        # professor = form.data['professor']
        # data_agendamento = form.data['data_agendamento']
        # horario_inicio = form.data['horario_inicio']
        # horario_fim = form.data['horario_fim']

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentoSerializer