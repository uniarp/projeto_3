from django.db import models

# Create your models here.

class Denuncia(models.Model):
    endereco = models.CharField(max_length=255)
    observacao = models.TextField()
    imagem = models.ImageField(upload_to='')
