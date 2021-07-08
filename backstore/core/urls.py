from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import ProductoViewSet, home, listado_prod, galeria_prod,valores,nuevo_producto,modificar_producto,eliminar_producto

from .views import ProductoSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',ProductoViewSet)

urlpatterns = [
    path('',home,name="home"),
    path('listado_prod/',listado_prod,name="listado_prod"),
    path('galeria_prod/',galeria_prod,name="galeria_prod"),
    path('valores/',valores,name="valores"),
    path('nuevo_producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar_producto<id>',modificar_producto,name="modificar_producto"),
    path('eliminar_producto<id>',eliminar_producto,name="eliminar_producto"),
    path('api/',include(router.urls)),
]