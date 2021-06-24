from .models import Producto
from django.shortcuts import render, redirect
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def listado_prod(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request,'core/listado_prod.html',data)

def galeria_prod(request):
    return render(request,'core/galeria_prod.html')

def valores(request):
    return render(request,'core/valores.html')

@permission_required('core.add_producto')
def nuevo_producto(request):
    data ={
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto agregado correctamente"
    return render(request,'core/nuevo_producto.html',data)

@permission_required('core.change_producto')
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto modificado correctamente"
        data['form'] = formulario
    return render(request, 'core/modificar_producto.html',data)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="listado_prod")
