from django.db import models
from django.db import models

# Create your models here.

class Usuario(models.Model) :
    nombre = models.CharField(max_length = 100)
    correo = models.EmailField(unique = True)
    contraseña = models.CharField(max_length = 100)
    es_proveedor = models.BooleanField(default = False)
    es_administrador = models.BooleanField(default = False)

class Proveedor(models.Model) : 
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'proveedor')
    biografia = models.TextField()
    detalles_contacto = models.TextField()
    detalles_banco = models.TextField()
    politica_envios = models.TextField()
    politica_reembolso = models.TextField()

class Categoria(models.Model) :
    nombre = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    padre = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'subcategoria')

    def __str__(self) :
        return self.nombre

class Producto(models.Model) : 
    proveedor = models.ForeignKey(Proveedor, on_delete= models.CASCADE, related_name = 'productos')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name= 'productos')
    nombre = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digit = 100, decimal_places = 2)
    cantidad = models.PositiveIntegerField()
    imagen = models.ImageField()
    creacion = models.DateTimeField(auto_now_add = True)
    actualizacion = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = 'orden')
    productos = models.ManyToManyField(Producto, through= 'articulo de pedido')
    precip_total = models.DecimalField(max_digits = 100, decimal_places = 2)
    direccion_envio = models.FileField()
    creacion = models.DateTimeField(auto_now_add = True)
    actualizacion = models.DateTimeField(auto_now = True)

class ArticuloPedido(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name = 'articulos')
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.PositiveIntegerField(default = 1)

class Cart(models.Model):
    usuario = models.fore