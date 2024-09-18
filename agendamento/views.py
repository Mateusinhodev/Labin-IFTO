from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Agendamentos, Laboratorios, Professores
from .forms import AgendamentoAula
from .serializers import AgendamentoSerializer
from rest_framework import viewsets
from datetime import datetime


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
                                                        'form': form,
                                                        'id_agendamento': id})
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

def excluir_agendamento(request, id):
    agendamento = Agendamentos.objects.get(id = id).delete()
    return redirect('/agendamento/home')

# def editar_agendamento(request):
#     agendamento_id = request.POST.get('agendamento_id')
#     laboratorio = request.POST.get('laboratorio')
#     professor = request.POST.get('professor')
#     data_agendamento = request.POST.get('data_agendamento')
#     inicio_aula = request.POST.get('inicio_aula')
#     final_aula = request.POST.get('final_aula')

#     # Converte a data_agendamento de string para datetime no formato 'YYYY-MM-DD'
#     try:
#         data_agendamento = datetime.strptime(data_agendamento, '%Y-%m-%d').date()
#     except ValueError:
#         # Lida com erro de formato de data, caso o usuário insira uma data inválida
#         return HttpResponse("Data inválida, por favor insira no formato YYYY-MM-DD")

#     agendamento = Agendamentos.objects.get(id = agendamento_id)
#     laboratorio = Laboratorios.objects.all()
#     professor = Professores.objects.all()

#     laboratorio.nome = laboratorio
#     professor.nome = professor
#     agendamento.data_agendamento = data_agendamento
#     agendamento.horario_inicio = inicio_aula
#     agendamento.horario_fim = final_aula
#     agendamento.save()

#     return redirect('/agendamento/ver_agendamento/{agendamento_id}')
class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentoSerializer