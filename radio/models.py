from django.db import models

class Radio(models.Model):
    Nome = models.CharField(max_length=255)
    Frequencia = models.CharField(max_length = 20)
    Logo = models.FileField(upload_to='./media/images')
    Link = models.CharField(max_length=255)
    def __str__(self):
        return self.Nome