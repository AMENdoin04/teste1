from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome