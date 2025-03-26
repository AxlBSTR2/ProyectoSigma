from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == "POST":
        username = request.POST['logUsuario']
        password = request.POST['password']
        User = authenticate(request, username = username, password = password)
        if User is not None:
            login(request, User)
            return redirect('index')
        else:
            messages.error(request, "Has tenido un error al iniciar sesión")
            return HttpResponseRedirect('.')
    else:
        return render(request, 'appSigma/logearse.html') 

def registrarse(request):
    return render(request, 'Mangas/registrarse.html')

def registro_view(request):
    if request.method != "POST":
        return render(request, 'appSigma/registrarse.html')
    else:
        username = request.POST.get('regNombre')
        email = request.POST.get('regEmail')
        password = request.POST.get('regContrasena')

        # Crea un nuevo objeto de usuario y establece los valores
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = username
        user.save()

        messages.success(request, "Cuenta creada exitosamente")

        return redirect('logearse')

def index(request):
    return render(request,'appSigma/index.html')

def contacto(request):
    return render(request, 'appSigma/contacto.html')

def carritocompra(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'appSigma/carritocompra.html', data)

def perfilusuario(request):
    return render(request, 'appSigma/perfilusuario.html')

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

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def eliminar_cuenta(request):
    if request.method == "POST":
        user = request.user
        logout(request)  # Cerrar sesión antes de eliminar
        user.delete()
        return redirect("home")  # Cambia "home" por la vista de inicio o login

    return redirect("perfil")  # Si alguien entra por GET, redirigir al perfil

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

def eliminar_cuenta(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()  # Elimina al usuario de la base de datos
        messages.success(request, "Tu cuenta ha sido eliminada con éxito.")
        return redirect('index')  # Redirige al inicio o a cualquier otra página
    else:
        messages.error(request, "No estás autenticado.")
        return redirect('index')  # O redirige a la página que quieras