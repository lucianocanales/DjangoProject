from django.db import models
from stdimage import StdImageField


class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=250)
    imagen = StdImageField(
        upload_to='servicios',
        variations={
            'medium': (640, 260, True),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 640 X 260'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Servicio"
        verbose_name = "Servicios"

    def __str__(self):
        return self.titulo
