from django.db import models
from django.contrib.auth.models import User
from apps.manager.models import Sucursal
from apps.sales.models import Cliente
from apps.inventory.models import Articulo, Transaccion

# Create your models here.

class Reparacion(models.Model):
	ESTADO = (
		(1,'Revision'),
		(2, 'Reparacion'),
		(3, 'Limpieza'),
		(2, 'Terminado'),
		)
	id_reparacion = models.PositiveIntegerField(max_length=10000)
	cliente = models.ForeignKey(Cliente)
	fecha = models.DateTimeField(auto_now=True,auto_now_add=True)
	mecanico = models.ForeignKey(User)
	comentario = models.CharField(max_length=50,null=True)
	servicio = models.CharField(max_length=1,choices=ESTADO,default=1)
	total_servicio = models.DecimalField(max_digits=20,decimal_places=2)
	total = models.DecimalField(max_digits=20,decimal_places=2)

	class Meta:
		verbose_name_plural = 'Reparaciones'

	def __unicode__(self):
		return u'%s' % self.id_reparacion

class ReparacionLinea(models.Model):
	id_reparacion = models.ForeignKey('Reparacion')
	articulo = models.ForeignKey('inventory.Articulo')
	sucursal = models.ForeignKey('manager.Sucursal')
	cantidad = models.PositiveIntegerField(max_length=1000)
	precio = models.DecimalField(max_digits=20,decimal_places=2)
	total_linea = models.DecimalField(max_digits=20,decimal_places=2,default=0)

	def save(self, *args, **kwargs):
		transaccion = Transaccion(tipo=2,articulo=self.articulo,sucursal=self.sucursal,
			cantidad=self.cantidad)
		transaccion.save()
		super(ReparacionLinea, self).save(*args, **kwargs)


	def __unicode__(self):
		return u'%s' % self.id_reparacion



