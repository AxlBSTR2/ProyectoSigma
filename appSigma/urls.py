from django.urls import path
from . import views
from .views import eliminar_cuenta
urlpatterns = [
    path('', views.index,name='index'),
    
    path('carritocompra/', views.carritocompra, name='carritocompra'),

    path('logearse/', views.login_user, name='logearse'),

    path('registrarse/', views.registro_view, name='registrarse'),

    path('perfilusuario/', views.perfilusuario, name='perfilusuario'),

    path('contacto/', views.contacto, name='contacto'),

    path('agregar-producto', views.agregar_producto, name='agregar-producto'),

    path('listar-producto', views.listar_producto, name='listar-producto'),

    path('modificar-producto/<id>', views.modificar_producto, name='modificar-producto'),

    path('eliminar-producto/<id>', views.eliminar_producto, name='eliminar-producto'),

    path('logout/', views.logout_user, name='logout'),

    path("eliminar-cuenta/", views.eliminar_cuenta, name="eliminar_cuenta")

]