from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'appSigma/index.html')

def contacto(request):
    return render(request, 'appSigma/contacto.html')

def carritocompra(request):
    return render(request, 'appSigma/carritocompra.html')

def logearse(request):
    return render(request, 'appSigma/logearse.html')

def perfilusuario(request):
    return render(request, 'appSigma/perfilusuario.html')

def registrarse(request):
    return render(request, 'appSigma/registrarse.html')

def seguimiento(request):
    return render(request, 'appSigma/seguimiento.html')

