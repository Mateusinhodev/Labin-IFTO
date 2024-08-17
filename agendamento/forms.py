from django import forms 
from .models import Agendamentos

class AgendamentoAula(forms.ModelForm):
    class Meta:
        model = Agendamentos
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)