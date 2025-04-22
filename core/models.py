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
<<<<<<< HEAD
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
=======
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length= 100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits= 100, decimal_places= 2)
    stock = models.PositiveBigIntegerField()
    imagen =models.ImageField(upload_to='productos')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en =models.DateTimeField(auto_now_add=True)
>>>>>>> ea2a417453e7aed694037b7e4966d9c13bac9ae3

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
<<<<<<< HEAD
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
=======
    cliente = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name='clientes')
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_total= models.DecimalField(max_digits=100, decimal_places=2)
    direccion_envio= models.FileField()
    creado_en = models.DateTimeField(auto_now_add= True)
    actualizado_en = models.DateTimeField(auto_now=True)

class ArticulodePedido(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Carro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'carro', null=True,blank=True)
    id_sesion = models.CharField(max_length=100,null=True,blank=True)
    items = models.ManyToManyField(Producto, through='ArticulodeCarrito')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en= models.DateTimeField(auto_now=True)

class ArticulodeCarrito(models.Model): 
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name= 'carro', null=True,blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Envio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tarifa = models.DecimalField(max_digits=10,decimal_places=2)

class Pago(models.Model):
    orden = models.ForeignKey(Orden, on_delete= models.CASCADE,related_name='pago')
    metodo = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10,decimal_places=2)
    id_transaccion = models.CharField(max_length=100)
    creado_en= models.DateTimeField(auto_now_add=True)

class Cupon(models.Model):
    codigo= models.CharField(max_length=100,unique=True)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
    valido_desde = models.DateTimeField()
    valido_para  = models.DateTimeField()

class Revisar(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='revisar')
    cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='revisar')
    clasificacion = models.PositiveIntegerField()
    comentario = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en= models.DateTimeField(auto_now=True)

class ListadeDeseos(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='notificaciones')
    productos =models.ManyToManyField(Producto, related_name='listadedeseo')

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name='notificacion')
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200, unique = True)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='blog_posts')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    creado_en= models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    pregunta =models.TextField()
    respuesta =models.TextField()

class Analitica(models.Model):
    ventas = models.DecimalField(max_digits=10,decimal_places=2)
    traffic = models.PositiveBigIntegerField()
    productos_populares = models.ManyToManyField(Producto,related_name='analitica')
    creado_en = models.DateTimeField(auto_now_add=True)

class Configuracion(models.Model):
    nombre_sitio= models.CharField(max_length=100)
    descripcion_sitio = models.TextField()
    logo_sitio = models.ImageField(upload_to='logos')

class Impuesto(models.Model):
    nombre = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100,null=True,blank=True)

class Subscripcion(models.Model):
    correo = models.EmailField(unique=True)
    subscrito_en = models.DateTimeField(auto_now_add=True)


class Reembolso(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='reembolsos')
    razon = models.TextField()
    cantidad = models.DecimalField(max_digits=5,decimal_places=2)
    estado = models.CharField(max_length=100)
    solicitada_en= models.DateTimeField(auto_now_add=True)
    procesado_en=models.DateTimeField(null=True,blank=True)



>>>>>>> ea2a417453e7aed694037b7e4966d9c13bac9ae3
