from django.db import models

class AnimaisAdocao(models.Model):
        nome = models.CharField(max_length=50)
        raca = models.CharField(max_length=50)
        condicaoSaude = models.CharField(max_length=50)
        imagem = models.ImageField(upload_to='')

class CadastroAnimal(models.Model):
    animal_id = models.IntegerField(max_length=20)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    
class Denuncia(models.Model):
    endereco = models.CharField(max_length=255)
    observacao = models.TextField()
    imagem = models.TextField()
    
