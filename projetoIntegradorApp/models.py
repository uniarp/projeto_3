from django.db import models
class AnimaisAdocao(models.Model):
        nome = models.CharField(max_length=50)
        raca = models.CharField(max_length=50)
        condicaoSaude = models.CharField(max_length=50)
        imagem = models.ImageField(upload_to='')
        