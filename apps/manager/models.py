from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
# MODELO PERFIL EXTIENDE EL MODELO USUARIO POR DEFECTO

class Perfil(models.Model):

    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    sucursal = models.ForeignKey('Sucursal')

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        return self.user.username

# MODELO SUCURSAL

class Sucursal(models.Model):

    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Sucursales'

    def __unicode__(self):
        return self.nombre

# MODELO FABRICANTE

class Fabricante(models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logofabricante')

    class Meta:
        verbose_name_plural = 'Fabricantes'


    def mostrarImagen(self):#sirve para que el campo logo me regrese la imagen del logo
        return """
        <img src="/media/%s" height='100'/>
        """ %self.photo.url
    mostrarImagen.allow_tags = True


    def __unicode__(self):
        return self.nombre