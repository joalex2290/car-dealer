from django.contrib import admin
from .models import Perfil, Sucursal

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
	pass
admin.site.register(Perfil,PerfilAdmin)

class SucursalAdmin(admin.ModelAdmin):
	pass
admin.site.register(Sucursal,SucursalAdmin)