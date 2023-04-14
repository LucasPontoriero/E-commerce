from django.urls import path

from .views import VRegistro, cerrar_sesion, logear

urlpatterns=[
    path('', VRegistro.as_view(), name="Autenticar"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('login/', logear, name="login" )
]