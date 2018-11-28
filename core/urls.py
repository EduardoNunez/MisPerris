from django.urls import path
from .views import home, formulario, agregarMascota, modificar_mascota, listar_mascotas, eliminar_mascota, login, get_ciudades

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
    path('listar_mascotas/', listar_mascotas, name="listar_mascotas"),
    path('agregarMascota/', agregarMascota, name="agregarMascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('get_ciudades/<id>/', get_ciudades, name="get_ciudades"),
]