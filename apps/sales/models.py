from django.db import models
from django.contrib.auth.models import User
from apps.manager.models import Sucursal
from apps.inventory.models import Articulo, Transaccion

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=10)
	apellido = models.CharField(max_length=10)
	cedula = models.PositiveIntegerField(max_length=10)
	telefono = models.PositiveIntegerField(max_length=10)
	direccion = models.CharField(max_length=30)
	email = models.EmailField()

	def __unicode__(self):
		return u'%s' % self.cedula

class Venta(models.Model):
	ESTADO = (
		(1,'Cotizacion'),
		(2, 'Venta'),
		)
	id_venta = models.PositiveIntegerField()
	cliente = models.ForeignKey('Cliente')
	estado = models.PositiveIntegerField(max_length=1,choices=ESTADO,default=1)
	fecha = models.DateTimeField(auto_now=True,auto_now_add=True)
	vendedor = models.ForeignKey(User)
	comentario = models.CharField(max_length=50)
	total = models.DecimalField(max_digits=20,decimal_places=2)

	def __unicode__(self):
		return self.id_venta

class VentaLinea(models.Model):
	id_venta = models.PositiveIntegerField()
	articulo = models.ForeignKey('inventory.Articulo')
	sucursal = models.ForeignKey('manager.Sucursal')
	cantidad = models.PositiveIntegerField()
	precio = models.DecimalField(max_digits=20,decimal_places=2)
	total_linea = models.DecimalField(max_digits=20,decimal_places=2,default=0)

	def save(self, *args, **kwargs):
		transaccion = Transaccion(tipo=3,articulo=self.articulo,sucursal=self.sucursal,
			cantidad=self.cantidad,usuario=user)
		transaccion.save()
		super(VentaLinea, self).save(*args, **kwargs)



