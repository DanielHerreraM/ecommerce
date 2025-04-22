from rest_framework import serializers
from .models import (
    Usuario, Proveedor, Categoria, Producto, Orden, ArticulodePedido, Carro,
    ArticulodeCarrito, Envio, Pago, Cupon, Revisar, ListadeDeseos, Notificacion,
    Blog, Contacto, FAQ, Analitica, Configuracion, Impuesto, Subscripcion, Reembolso
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ' __all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ' __all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ' __all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only =True)
    proveedor = ProveedorSerializer(read_only =True)
    reviews = serializers.StringRelatedField(many = True, read_only =True)
    class Meta:
        model = Producto
        fields = ' __all__'

class OrdenSerializer(serializers.ModelSerializer):
    cliente = UsuarioSerializer(read_only =True)
    producto = ProductoSerializer(read_only =True)
    class Meta:
        model = Orden
        fields = ' __all__'

class ArticulodePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticulodePedido
        fields = ' __all__'

class CarroSerializer(serializers.ModelSerializer):
    items = ProductoSerializer(read_only =True)
    class Meta:
        model = Carro
        fields = ' __all__'

class ArticulodeCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticulodeCarrito
        fields = ' __all__'
    
class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = ' __all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ' __all__'

class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ' __all__'

class RevisarSerializer(serializers.ModelSerializer):
    cliente = UsuarioSerializer(read_only =True)
    class Meta:
        model = Revisar
        fields = ' __all__'

class ListadeDeseosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListadeDeseos
        fields = ' __all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = ' __all__'

class BlogSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ' __all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ' __all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ' __all__'

class AnaliticaSerializer(serializers.ModelSerializer):
    productos_populares = ProductoSerializer(many = True,read_only=True)
    class Meta:
        model = Analitica
        fields = ' __all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ' __all__'

class ImpuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impuesto
        fields = ' __all__'

class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscripcion
        fields = ' __all__'

class ReembolsoSerializer(serializers.ModelSerializer):
    orden= OrdenSerializer(read_only=True)
    class Meta:
        model = Reembolso
        fields = ' __all__'
