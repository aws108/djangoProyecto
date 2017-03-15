from django.contrib import admin

from .models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'cantidad', 'detalles','pub_date')


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)

