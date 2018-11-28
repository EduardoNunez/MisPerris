from django.contrib import admin
from .models import Region, Ciudad, Tipo_Vivienda, Postulante, Raza, Estado, Mascota, Genero #Comuna

# Register your models here.
#clase de configuracion para
#el automovil en el admin de django
class PostulanteAdmin(admin.ModelAdmin):

    #declaramos una tupla
    list_display = ('correo_electronico', 'run', 'nombre_completo', 'fecha_nacimiento', 'telefono_contacto', 'region', 'ciudad', 'tipo_vivienda')
    search_fields = ['run', 'nombre_completo']

    #agregaremos un filtro personalizado en el admin
    list_filter = ('region','ciudad')

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre_mascota','raza_mascota','genero_mascota','fecha_Ingreso','fecha_Nacimiento_Mascota', 'imagen_Mascota','estado_Mascota')

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Tipo_Vivienda)
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Genero)
#admin.site.register(Comuna)