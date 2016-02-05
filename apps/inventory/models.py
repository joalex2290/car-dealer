from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from apps.manager.models import Fabricante, Sucursal

# Create your models here.

# MODELO ARTICULO

class Articulo(models.Model):
    TIPO_ARTICULO = (
        (1, 'Vehiculo'),
        (2, 'Repuesto'),
    )
    codigo = models.CharField(max_length=10)
    tipo = models.PositiveIntegerField(max_length=1,choices=TIPO_ARTICULO)
    fabricante = models.ForeignKey('manager.Fabricante')
    descripcion = models.CharField(max_length=50)
    modelo = models.PositiveIntegerField(max_length=4, help_text='YYYY')
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_articulos')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Articulos'

    def mostrarImagen(self):#sirve para que el campo logo me regrese la imagen del logo
        return """
        <img src="/media/%s" height='100'/>
        """ %self.photo.url
    mostrarImagen.allow_tags = True

    def __unicode__(self):
        return self.codigo + ' - ' + self.descripcion + ' ' + str(self.modelo)

class Stock(models.Model):
    articulo = models.ForeignKey('Articulo')
    sucursal = models.ForeignKey('manager.Sucursal')
    stock = models.PositiveIntegerField()

    class Meta:
        unique_together = ("articulo", "sucursal")
        verbose_name_plural = 'Stocks'

    def __unicode__(self):
        return self.id

class Transaccion(models.Model):
    TIPO_TRANSACCION = (
        (1, 'Entrada'),
        (2, 'Salida'),
        (3, 'Venta'),
        (4, 'Reparacion'),
    )
    tipo = models.PositiveIntegerField(max_length=1,choices=TIPO_TRANSACCION)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(null=0)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=True)
    usuario = models.ForeignKey(User)
    comentario = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = 'Transacciones'

    def __unicode__(self):
        return u'%s' % self.fecha

    def save(self, *args, **kwargs):

        try:
            stock = Stock.objects.get(articulo=self.articulo,sucursal=self.sucursal)
        except:
            stock = Stock(articulo=self.articulo, sucursal=self.sucursal, stock=0)

        if self.tipo is 1:
            stock.stock = stock.stock+self.cantidad
        else:
            stock.stock = stock.stock-self.cantidad

        if stock.stock >= 0:
            stock.save()
            super(Transaccion, self).save(*args, **kwargs)
        else:
            raise ValidationError('La cantidad solicitada supera el Stock actual.')
        
            
        
