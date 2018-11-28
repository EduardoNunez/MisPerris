from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json
from core.models import Mascota, Raza, Genero, Estado

# Para limitar un metodo a un tipo de peticion.
from django.views.decorators.http import require_http_methods

# Solucionar un error (PENDIENTE).
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    # Obtenemos el token.
    token = bodyDict['token']

    # Primero verificamos que el token no exista en la BBDD para guardarlo.
    # ***********************IMPORTANTE********************** 
       
    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe: 
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe'}), content_type ="aplication/json")

    # ***********************IMPORTANTE********************** 

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    # Solo si el usuario esta autenticado lo asociaremos con el token.
    if request.user.is_authenticated:
        dispositivo.user = request.user
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'El Token fue almacenado'}), content_type ="aplication/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se ha podido guardar el Token'}), content_type ="aplication/json")


# Crearemos un view que muestre el listado de automoviles en formato Json.

def listar_mascotas(request):
    mascotitas = Mascota.objects.all()

    mascotitasJson = serializers.serialize('json', mascotitas)

    return HttpResponse(mascotitasJson, content_type="application/json")

# POST
@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascotas(request):
    # Obtenemos el body del request.
    body = request.body.decode('utf-8')
    # El body viene como un String por lo que lo transformamos.
    bodyDict = json.loads(body)

    # Guardaremos la mascota en la BBDD.
    mascota = Mascota()
    mascota.nombre_mascota = bodyDict['nombre_mascota']
    mascota.raza_mascota = Raza(id=bodyDict['raza_id'])
    mascota.genero_mascota = Genero(id=bodyDict['genero_id'])
    mascota.fecha_Nacimiento_Mascota = bodyDict['fecha_Nacimiento_Mascota']
    mascota.fecha_Ingreso = bodyDict['fecha_Ingreso']
    mascota.imagen_Mascota = bodyDict['imagen_Mascota']
    mascota.estado_Mascota = Estado(id=bodyDict['estado_id'])

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado Correctamente'}), content_type="application/json")

    except:
        # Retornaremos un mensaje con codigo de error.
        return HttpResponseBadRequest(json.dumps({'mensaje':'No Se Ha Podido Guardar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        # Primero buscamos la mascota que eliminaremos
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje':'Eliminado correctamente'}), 
        content_type ="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se ha podido eliminiar'}), 
        content_type ="application/json")

# PUT
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    # Obtenemos el body del request.
    body = request.body.decode('utf-8')
    # El body viene como un String por lo que lo transformamos.
    bodyDict = json.loads(body)

    mascota = Mascota()
    mascota.id = bodyDict['id']
    mascota.nombre_mascota = bodyDict['nombre_mascota']
    mascota.raza_mascota = Raza(id=bodyDict['raza_id'])
    mascota.genero_mascota = Genero(id=bodyDict['genero_id'])
    mascota.fecha_Nacimiento_Mascota = bodyDict['fecha_Nacimiento_Mascota']
    mascota.fecha_Ingreso = bodyDict['fecha_Ingreso']
    mascota.imagen_Mascota = bodyDict['imagen_Mascota']
    mascota.estado_Mascota = Estado(id=bodyDict['estado_id'])

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado Correctamente'}), content_type="application/json")

    except:
        # Retornaremos un mensaje con codigo de error.
        return HttpResponseBadRequest(json.dumps({'mensaje':'No Se Ha Podido modificar'}), content_type="application/json")

