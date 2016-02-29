from django.contrib import admin
from .models import Reparacion, ReparacionLinea

# Register your models here.

# Register your models here.

class ReparacionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reparacion,ReparacionAdmin)

class ReparacionLineaAdmin(admin.ModelAdmin):
	pass
admin.site.register(ReparacionLinea,ReparacionLineaAdmin)