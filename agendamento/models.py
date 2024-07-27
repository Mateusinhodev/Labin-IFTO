from django.db import models

# Modelagem do Banco de dados.

class Laboratorios(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Laboratório'

    def __str__(self) -> str:
        return self.nome

class Professores(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Professore'

    def __str__(self) -> str:
        return self.nome

class Agendamentos(models.Model):
    professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)
    laboratorio = models.ForeignKey(Laboratorios, on_delete=models.DO_NOTHING)
    data_agendamento = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    class Meta:
        verbose_name = 'Agendamento'

    def __str__(self):
        return f"{self.professor} - {self.laboratorio} - {self.data_agendamento}"
