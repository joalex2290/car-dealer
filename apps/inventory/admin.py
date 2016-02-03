from django.contrib import admin
from .models import Articulo, Stock, Transaccion


# Register your models here.

# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
	pass
admin.site.register(Articulo,ArticuloAdmin)

class StockAdmin(admin.ModelAdmin):
	pass
admin.site.register(Stock,StockAdmin)

class TransaccionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Transaccion,TransaccionAdmin)