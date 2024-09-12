from django.db import models


class CadastroTutor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=15)
    financas = models.DecimalField(max_digits=10, decimal_places=2)

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
    

