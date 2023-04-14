from django.shortcuts import redirect

from .carro import Carro
from App.models import Productos

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Home") 

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Home")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Home")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Home")