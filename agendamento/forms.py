from django import forms 
from .models import Agendamentos

class AgendamentoAula(forms.ModelForm):
    class Meta:
        model = Agendamentos
        fields = "__all__"