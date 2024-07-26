from django.contrib import admin
from .models import Usuario

# Área Administrativ.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')