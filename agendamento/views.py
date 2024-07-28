from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Agendamentos, Laboratorios, Professores

# É onde encontra se toda a lógica do sistema.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        agendamentos = Agendamentos.objects.all()
        return render(request, 'home.html', {'agendamentos': agendamentos})
    else: 
        return redirect('/auth/login/?status=2')
    
def ver_agendamento(request, id):
    if request.session.get('usuario'):
        agendamento = Agendamentos.objects.get(id = id)
        laboratorio = Laboratorios.objects.all()
        professor = Professores.objects.all()
        return render(request, 'ver_agendamento.html', {'agendamento': agendamento,
                                                        'laboratorio': laboratorio,
                                                        'professor': professor})
    return redirect('/auth/login/?status=2')