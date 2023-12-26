from django.shortcuts import render
from . import models

def index(request):
    pessoa = models.Pessoas.objects.all()
    imagens_carosels = models.Imagem_carosel.objects.all()
    for imagem in imagens_carosels:
        if imagem.lugar == "pri":
            pri = imagem.img.url
        if imagem.lugar == "seg":
            seg = imagem.img.url
        if imagem.lugar == "ter":
            ter = imagem.img.url
    return render(request, 'index.html', {'pessoas': pessoa, "pri": pri, "seg": seg, "ter": ter})