from django.db import models

# Create your models here.
 
class Region(models.Model):
    nombre_region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_region

    class Meta:
        verbose_name="Region"
        verbose_name_plural = "Regiones"

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)
    #clave foranea
    region  = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_ciudad
    def as_dict(self):
        return {
            "id": self.id,
            "nombre_ciudad":self.nombre_ciudad,
        }
    class Meta:
        verbose_name="Ciudad"
        verbose_name_plural = "Ciudades"  

#class Comuna(models.Model):
#    nombre_comuna= models.CharField(max_length=250)
#    ciudad  = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

#    def _str_(self):
#        return self.nombre_comuna
#    def as_dict(self):
#        return {
#            "id": self.id,
#            "nombre_comuna":self.nombre_comuna,
#        }
#    class Meta:
#        verbose_name="Comuna"
#        verbose_name_plural = "Comunas"  

class Tipo_Vivienda(models.Model):
    nombre_tipoVivienda = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipoVivienda

    class Meta:
        verbose_name="Tipo Vivienda"
        verbose_name_plural = "Tipo de Viviendas"

class Postulante(models.Model):
    correo_electronico = models.CharField(max_length=100)
    run = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono_contacto = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    tipo_vivienda = models.ForeignKey(Tipo_Vivienda, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.correo_electronico
        return self.run
        return self.nombre_completo
        return self.fecha_nacimiento
        return self.telefono_contacto
        return self.region
        return self.tipo_vivienda
        return self.ciudad

class Raza(models.Model):
    raza = models.CharField(max_length=50)

    def __str__(self):
        return self.raza

class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Genero(models.Model):
    genero_mascota = models.CharField(max_length=1)

    def __str__(self):
        return self.genero_mascota

    def genero_formato(self):

        if self.genero_mascota == 'M':
            genero = "Macho"
        else:
            genero = "Hembra"

        return genero

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=50)
    raza_mascota = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero_mascota = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_Nacimiento_Mascota = models.DateField(null=True, )
    fecha_Ingreso = models.DateField(null=True, blank=True)
    imagen_Mascota = models.FileField(upload_to="media/", blank=True, null=True)
    estado_Mascota = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_mascota
        return self.raza_mascota
        return self.genero_mascota
        return self.fecha_Nacimiento_Mascota
        return self.fecha_Ingreso
        return self.imagen_Mascota
        return self.estado_Mascota
    
    def fecha_ingreso_formato(self):
        return self.fecha_Ingreso.strftime("%Y-%m-%d")

    def fecha_nacimiento_formato(self):
        return self.fecha_Nacimiento_Mascota.strftime("%Y-%m-%d")

    def genero_formato(self):

        if self.genero_mascota_id == 1:
            genero = "Macho"
        else:
            genero = "Hembra"

        return genero
    
    # @property
    # def imagen_Mascota_url(self):#para mostrar la foto en la lista y en otros medios
    #     if self.imagen_Mascota and hasattr(self.imagen_Mascota, 'url'):
    #         return self.imagen_Mascota.url
    #     else:
    #         return "sinfoto"

    # @property
    # def imagen_Mascota(self):
    #     if self.imagen_Mascota and hasattr(self.imagen_Mascota, 'url'):
    #         return "as"
    #     else:
    #         return None

