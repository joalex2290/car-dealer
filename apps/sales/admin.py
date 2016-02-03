from django.contrib import admin
from .models import Cliente, Venta, VentaLinea

# Register your models here.

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Cliente,ClienteAdmin)

class VentaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Venta,VentaAdmin)

class VentaLineaAdmin(admin.ModelAdmin):
	pass
admin.site.register(VentaLinea,VentaLineaAdmin)