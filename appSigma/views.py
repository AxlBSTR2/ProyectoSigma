from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request,'appSigma/index.html')

def contacto(request):
    return render(request, 'appSigma/contacto.html')

def carritocompra(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'appSigma/carritocompra.html', data)

def logearse(request):
    return render(request, 'appSigma/logearse.html')

def perfilusuario(request):
    return render(request, 'appSigma/perfilusuario.html')

def registrarse(request):
    return render(request, 'appSigma/registrarse.html')

def seguimiento(request):
    return render(request, 'appSigma/seguimiento.html')

def agregar_producto(request):
    data = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario
    return render(request, 'appSigma/producto/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'appSigma/producto/listar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "modificado Correctamente"
            return redirect(to='listar-producto')  
        data['form'] = formulario
    return render(request, 'appSigma/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar-producto")