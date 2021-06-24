from django.contrib import admin
from .models import Empresa, Producto

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
        list_display = ['nombre','tipo','descripcion','precio','empresa']
        search_fields = ['nombre','tipo']
        list_filter = ['tipo']
        list_per_page = 5

admin.site.register(Empresa)
admin.site.register(Producto,ProductosAdmin)
