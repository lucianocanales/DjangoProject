from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField

# Create your models here.


class Caracteristica(models.Model):
    nombre = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Caracteristica"
        verbose_name = "Caracteristicas"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    padre = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Categoria"
        verbose_name = "Cateegorias"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    estado_choices = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('virtual', 'Virtual'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.FloatField()
    ventas = models.IntegerField(default=0)
    estado = models.CharField(
        max_length=50,
        choices=estado_choices,
        default='Nuevo'
    )
    caracteristica = models.ManyToManyField(Caracteristica)
    stock = models.IntegerField(default=0)
    categorias = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        default=None)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Producto"
        verbose_name = "Productos"

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    estados_choices = [
        ('active', 'Activa'),
        ('Inactiva', 'Inactiva'),
    ]
    imagen = StdImageField(
        variations={
            'medium': (350, 350),
            'thumbnail': (100, 100),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350',
        upload_to='productos',
        null=True,
        blank=True)
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='Inactiva',
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Imagen"
        verbose_name = "Imagenes"


class ImagenProducto(models.Model):
    caracteristica = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        verbose_name='Producto',
    )
    image = models.ForeignKey(
        Imagen,
        on_delete=models.CASCADE,
        verbose_name='Imagen',
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Imagen de producto"
        verbose_name = "Imagenes de productos"

    def __str__(self):
        return self.caracteristica.nombre + ' imagen: ' + str(self.image.id)


class ImageCarousel(models.Model):
    imagen = StdImageField(
        upload_to='productos/carousel',
        null=True,
        blank=True,
        variations={
            'medium': (1600, 600, True),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 1600 X 600'
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Imagen del carrusel"
        verbose_name = "Imagenes del carrusel"
