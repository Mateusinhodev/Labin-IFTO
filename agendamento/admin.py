from django.contrib import admin
from .models import Agendamentos, Laboratorios, Professores

# Register your models here.

admin.site.register(Laboratorios)
admin.site.register(Professores)
admin.site.register(Agendamentos)


