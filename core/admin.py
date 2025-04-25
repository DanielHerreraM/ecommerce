from django.contrib import admin
from .models import (
    Usuario, Proveedor, Categoria, Producto, Orden, ArticulodePedido, Carro,
    ArticulodeCarrito, Envio, Pago, Cupon, Revisar, ListadeDeseos, Notificacion,
    Blog, Contacto, FAQ, Analitica, Configuracion, Impuesto, Subscripcion, Reembolso
)

admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(ArticulodePedido)
admin.site.register(Carro)
admin.site.register(ArticulodeCarrito)
admin.site.register(Envio)
admin.site.register(Pago)
admin.site.register(Cupon)
admin.site.register(Revisar)
admin.site.register(ListadeDeseos)
admin.site.register(Notificacion)
admin.site.register(Blog)
admin.site.register(Contacto)
admin.site.register(FAQ)
admin.site.register(Analitica)
admin.site.register(Configuracion)
admin.site.register(Impuesto)
admin.site.register(Subscripcion)
admin.site.register(Reembolso)

