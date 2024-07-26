from django.shortcuts import render
from django.http import HttpResponse

# É onde encontra se toda a lógica do sistema.

def cadastrar(request):
    return HttpResponse('Olá')