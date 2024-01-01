from django.db import models

class Integrantes(models.Model):
    Nome_integrante = models.CharField(max_length=255)
    Telefone = models.IntegerField()
    def __str__(self):
        return self.Nome_integrante