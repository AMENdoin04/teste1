from django.contrib import admin
from .models import Pessoas, Imagem_carosel

admin.site.register(Pessoas)

@admin.action(description="remover imagem junto")
def remover_imagem(modeladmin, request, queryset):
    for evento in queryset:
        print(f"{settings.MEDIA_ROOT}/{evento.img}")
        os.remove(f"{settings.MEDIA_ROOT}/{evento.img}")

@admin.register(Imagem_carosel)
class EventosAdmin(admin.ModelAdmin):
    actions = [remover_imagem,]