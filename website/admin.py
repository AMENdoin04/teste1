from django.contrib import admin
from .models import Pessoas, Imagem_carosel

admin.site.register(Pessoas)

@admin.register(Imagem_carosel)
class EventosAdmin(admin.ModelAdmin):
    actions = [remover_imagem,]