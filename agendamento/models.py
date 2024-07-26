from django.db import models

# Modelagem do Banco de dados.

class Agendamentos(models.Model):
    professor = models.CharField(max_length= 100)
    laboratorio = models.CharField(max_length= 30)
    data_agendamento = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    class Meta:
        verbose_name = 'Agendamento'

    def __str__(self):
        return f"{self.professor} - {self.laboratorio} - {self.data_agendamento}"
