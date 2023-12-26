from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome

class Imagem_carosel(models.Model):
    lugar = models.TextField(max_length=255)
    img = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.lugar
