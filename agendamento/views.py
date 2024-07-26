from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario

# É onde encontra se toda a lógica do sistema.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        return HttpResponse (f'Olá {usuario}')
    else: 
        return redirect('/auth/login/?status=2')