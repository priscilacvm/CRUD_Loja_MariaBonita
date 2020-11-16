from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    Bairro = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome