from django.urls import path
from .views import listar_mascotas, agregar_mascotas, eliminar_mascota, modificar_mascota, agregar_token

urlpatterns = [
    path('listar-mascotas/', listar_mascotas, name="api_listar_mascotas"),
    path('agregar-mascotas/', agregar_mascotas, name="api_agregar_mascotas"),

    #La URL recibe el ID a eliminar.
    path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar-mascota/', modificar_mascota, name="api_modificar_mascota"),
    path('agregar-token/', agregar_token, name="api_agregar_token"),
]