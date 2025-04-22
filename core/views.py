from rest_framework import viewsets
from .models import (
    Usuario, Proveedor, Categoria, Producto, Orden, ArticulodePedido, Carro,
    ArticulodeCarrito, Envio, Pago, Cupon, Revisar, ListadeDeseos, Notificacion,
    Blog, Contacto, FAQ, Analitica, Configuracion, Impuesto, Subscripcion, Reembolso
)

from .serializers import(
    UsuarioSerializer,ProveedorSerializer,CategoriaSerializer,ProductoSerializer,
    OrdenSerializer,ArticulodePedidoSerializer,CarroSerializer,ArticulodeCarritoSerializer,
    EnvioSerializer,PagoSerializer,CuponSerializer,RevisarSerializer,ListadeDeseosSerializer,
    NotificacionSerializer,BlogSerializer,ContactoSerializer,FAQSerializer,AnaliticaSerializer,
    ConfiguracionSerializer,ImpuestoSerializer,SubscripcionSerializer,ReembolsoSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    
class ArticulodePedidoViewSet(viewsets.ModelViewSet):
    queryset = ArticulodePedido.objects.all()
    serializer_class = ArticulodePedidoSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset =  Carro.objects.all()
    serializer_class = CarroSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ArticulodeCarritoViewSet(viewsets.ModelViewSet):
    queryset = ArticulodeCarrito.objects.all()
    serializer_class = ArticulodeCarritoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class RevisarViewSet(viewsets.ModelViewSet):
    queryset = Revisar.objects.all()
    serializer_class = RevisarSerializer

class ListadeDeseosViewSet(viewsets.ModelViewSet):
    queryset = ListadeDeseos.objects.all()
    serializer_class = ListadeDeseosSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class AnaliticaViewSet(viewsets.ModelViewSet):
    queryset = Analitica.objects.all()
    serializer_class = AnaliticaSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class ImpuestoViewSet(viewsets.ModelViewSet):
    queryset = Impuesto.objects.all()
    serializer_class = ImpuestoSerializer

class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer


class ReembolsoViewSet(viewsets.ModelViewSet):
    queryset = Reembolso.objects.all()
    serializer_class = ReembolsoSerializer
