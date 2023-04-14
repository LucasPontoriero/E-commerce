from django.contrib import admin
from .models import Categoria, Productos

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Productos, ProductosAdmin)