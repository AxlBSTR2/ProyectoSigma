from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    
    path('carritocompra/', views.carritocompra, name='carritocompra'),

    path('logearse/', views.logearse, name='logearse'),

    path('registrarse/', views.registrarse, name='registrarse'),

    path('perfilusuario/', views.perfilusuario, name='perfilusuario'),

    path('seguimiento/', views.seguimiento, name='seguimiento'),

    path('contacto/', views.contacto, name='contacto')

]