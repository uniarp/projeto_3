from django.db import models

class CadastroTutor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=15)
    financas = models.DecimalField(max_digits=10, decimal_places=2)
