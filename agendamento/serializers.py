from rest_framework import serializers
from .models import Agendamentos

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'