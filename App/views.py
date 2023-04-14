from django.shortcuts import render

from carro.carro import Carro
from .models import Productos

def home(request):
    product=Productos.objects.all()
    carro=Carro(request)
    return render (request, 'App/home.html', {"product": product})





