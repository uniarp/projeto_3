from django.db import models

class Animal(models.Model):
    animal_id = models.IntegerField(max_length=20)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    dados_de_nascimento = models.CharField(max_length=50)