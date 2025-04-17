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

