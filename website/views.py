from django.shortcuts import render
from . import models

def index(request):
    pessoa = models.Pessoas.objects.all()
    return render(request, 'index.html', {'pessoas': pessoa})