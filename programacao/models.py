from django.db import models

class Programacao(models.Model):
    nome_programacao = models.CharField(max_length = 100)
    horario = models.TimeField()
    loucutor = models.CharField(max_length = 100)
    detalhes = models.TextField(null=True)
    turno = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_programacao