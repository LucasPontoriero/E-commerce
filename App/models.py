from django.db import models



class Categoria(models.Model):
    nombre=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="productos", null=True, blank=True)
    disponibilidad=models.BooleanField(default=True)
    precio=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

