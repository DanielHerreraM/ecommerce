from django.urls import path, include
from rest_framework import routers
from .views import (
    UsuarioViewSet,ProveedorViewSet,CategoriaViewSet,ProductoViewSet,
    OrdenViewSet,ArticulodePedidoViewSet,CarroViewSet,ArticulodeCarritoViewSet,
    EnvioViewSet,PagoViewSet,CuponViewSet,RevisarViewSet,ListadeDeseosViewSet,
    NotificacionViewSet,BlogViewSet,ContactoViewSet,FAQViewSet,AnaliticaViewSet,
    ConfiguracionViewSet,ImpuestoViewSet,SubscripcionViewSet,ReembolsoViewSet
)

router = routers.DefaultRouter()
router.register(r'usuario',UsuarioViewSet)
router.register(r'proveedor',ProveedorViewSet)
router.register(r'categorias',CategoriaViewSet)
router.register(r'productos',ProductoViewSet)
router.register(r'ordenes',OrdenViewSet)
router.register(r'articulospedidos',ArticulodePedidoViewSet)
router.register(r'carros',CarroViewSet)
router.register(r'articuloscarritos',ArticulodeCarritoViewSet)
router.register(r'envios',EnvioViewSet)
router.register(r'pagos',PagoViewSet)
router.register(r'cupones',CuponViewSet)
router.register(r'revisar',RevisarViewSet)
router.register(r'listadedeseos',ListadeDeseosViewSet)
router.register(r'notificaciones',NotificacionViewSet)
router.register(r'blogs',BlogViewSet)
router.register(r'contactos',ContactoViewSet)
router.register(r'FAQ',FAQViewSet)
router.register(r'analiticas',AnaliticaViewSet)
router.register(r'configuraciones',ConfiguracionViewSet)
router.register(r'impuestos',ImpuestoViewSet)
router.register(r'subscripciones',SubscripcionViewSet)
router.register(r'reemboslos',ReembolsoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
