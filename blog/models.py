from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from stdimage import StdImageField
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Categoria"
        verbose_name = "Cateegorias"

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField(blank=True, null=True)
    imagen = StdImageField(upload_to='post', null=True, blank=True, variations={
        'medium': (350, 350),
        'thumbnail': (128, 128, True),
    },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Post"
        verbose_name = "Posts"

    def __str__(self):
        return self.titulo
