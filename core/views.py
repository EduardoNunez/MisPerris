from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from .models import Region, Ciudad, Genero, Mascota, Postulante, Tipo_Vivienda, Raza, Estado #Comuna
# Create your views here.

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from fcm_django.models import FCMDevice

# Permisos para la mascota.
from django.contrib.auth.decorators import permission_required

def home(request):
    m_slider = Mascota.objects.filter(estado_Mascota_id=1)
    #Aquí hicimos una variable mascotas que almacena a todas las mascotas
    m_galeria = Mascota.objects.filter(estado_Mascota_id=2)
    variables = {
        'm_slider':m_slider,
        'm_galeria':m_galeria,

    }

    return render(request,'core/home.html', variables)

def formulario(request):
    #Rescatamos las regiones
    regiones = Region.objects.all()
    #Rescatamos las ciudades
    ciudades = Ciudad.objects.all()

    #comunas = Comuna.objects.all()

    #Rescatamos las viviendas
    tiposVivienda = Tipo_Vivienda.objects.all()

    #las metemos en un arreglo
    variables = {
        'regiones' : regiones,
        'ciudades' : ciudades,
        'tiposVivienda' : tiposVivienda
        #'comunas':comunas
    }
    
    if request.POST:
        postulante = Postulante()
        postulante.correo_electronico = request.POST.get('txtCorreo')
        postulante.run = request.POST.get('txtRun')
        postulante.nombre_completo = request.POST.get('txtNombre')
        postulante.fecha_nacimiento = request.POST.get('fecha')
        postulante.telefono_contacto = request.POST.get('txtTelefono')
        region = Region()
        region.id = request.POST.get('cboRegion')
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        tipo_vivienda = Tipo_Vivienda()
        tipo_vivienda.id = request.POST.get('cboTipoViv')
        postulante.region = region
        postulante.ciudad = ciudad
        postulante.tipo_vivienda = tipo_vivienda

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar correctamente'

    return render(request,'core/formulario.html', variables) 

def login(request):
    return render(request, 'core/login.html')

@login_required
@permission_required('Mascota.puede_agregar')
def agregarMascota(request):

    generos = Genero.objects.all()
    razas = Raza.objects.all()
    estados = Estado.objects.all()

    #las metemos en un arreglo
    variables = {
        'generos' : generos,
        'razas' : razas,
        'estados' : estados,
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombre_mascota = request.POST.get('txtMascota')
        mascota.fecha_Ingreso = request.POST.get('fechaIngreso')
        mascota.fecha_Nacimiento_Mascota = request.POST.get('fechaNacimiento')
        mascota.imagen_Mascota = request.FILES.get('imagen')
        estado_mascota = Estado()
        estado_mascota.id = request.POST.get('cboEstado')
        raza_mascota = Raza()
        raza_mascota.id = request.POST.get('cboRaza')
        genero_mascota = Genero()
        genero_mascota.id = request.POST.get('cboGenero')
        mascota.raza_mascota = raza_mascota 
        mascota.estado_Mascota = estado_mascota
        mascota.genero_mascota = genero_mascota

        try:
            mascota.save()

            # obtenemos todos los dispositivos.
            dispositivos = FCMDevice.objects.all()
            # A cada dispositivo se le envie una notificacion.
            dispositivos.send_message(
                title="Alerta MisPerris",
                body="Se ha agregado una nueva mascota",
                icon="/static/core/img/mascota_logo.png"
            )
            # 

            variables['mensaje'] = 'Se ha guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar correctamente'

    return render(request,'core/agregarMascota.html', variables)

def listar_mascotas(request):

    mascotas = Mascota.objects.all() 
    #Aquí hicimos una variable mascotas que almacena a todas las mascotas

    variables = {
        'mascotas':mascotas,
    }

    return render(request, 'core/listar_mascotas.html', variables) 

def eliminar_mascota(request, id):
    #Buscar la mascota que queremos eliminar
    mascota = Mascota.objects.get(id=id)
    
    try:
        mascota.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar esta mascota"
        messages.error(request, mensaje)

    return redirect('listar_mascotas') 

@login_required
def modificar_mascota(request, id):
    #Buscamos la mascota para que se puedan modificar sus datos
    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    generos = Genero.objects.all()

    variables = {
        'mascota':mascota,
        'razas':razas,
        'estados':estados,
        'generos':generos
        
    }

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombre_mascota = request.POST.get('txtMascota')
        mascota.fecha_Ingreso = request.POST.get('fechaIngreso')
        mascota.fecha_Nacimiento_Mascota = request.POST.get('fechaNacimiento')
        mascota.imagen_Mascota = request.FILES.get('imagen')
        estado_mascota = Estado()
        estado_mascota.id = request.POST.get('cboEstado')
        raza_mascota = Raza()
        raza_mascota.id = request.POST.get('cboRaza')
        genero_mascota = Genero()
        genero_mascota.id = request.POST.get('cboGenero')
        mascota.raza_mascota = raza_mascota 
        mascota.estado_Mascota = estado_mascota
        mascota.genero_mascota = genero_mascota 

        try:
            mascota.save()
            messages.success(request, 'Modificado correctamente')
        except:
            messages.error(request, 'No se ha podido modificar')
        return redirect('listar_mascotas') #Le estamos diciendo que si no se pudo modificar, que devuelva a la lista
    
    return render(request, 'core/modificar_mascota.html', variables )

def get_ciudades(request, id):
    ciudades=Ciudad.objects.filter(region=id)
    qs_json = serializers.serialize('json', ciudades)
    return HttpResponse(qs_json, content_type='application/json')
    
#def get_comunas(request, id):
    #comunas=Comuna.objects.filter(ciudad=id)
    #qs_json = serializers.serialize('json', comunas)
    #return HttpResponse(qs_json, content_type='application/json')