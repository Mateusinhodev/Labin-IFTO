from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Agendamentos

# É onde encontra se toda a lógica do sistema.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        agendamentos = Agendamentos.objects.all()
        return render(request, 'home.html', {'agendamentos': agendamentos})
    else: 
        return redirect('/auth/login/?status=2')
    
def ver_agendamento(request, id):
    agendamento = Agendamentos.objects.get(id = id)
    print(agendamento)
    return render(request, 'ver_agendamento.html', {'agendamento': agendamento})