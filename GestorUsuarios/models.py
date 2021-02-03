from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Email')
    bio = models.TextField(max_length=500, blank=True,
                           verbose_name='Descripcion')
    followers = models.IntegerField(verbose_name='Seguidores', default=0)
    following = models.IntegerField(verbose_name='Seguidos', default=0)
    friends = models.IntegerField(verbose_name='Amigos', default=0)
    busines = models.CharField(
        verbose_name='Empresa', max_length=300, blank=True, null=True)

    image_profile = StdImageField(
        variations={
            'medium': (350, 350),
            'thumbnail': (100, 100),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350',
        upload_to='profile',
        null=True,
        blank=True)
    objects = models.Manager()


'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''


class ImagesBio(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    image_bio = StdImageField(
        variations={
            'medium': (350, 350),
            'thumbnail': (100, 100),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350',
        upload_to='profile',
        null=True,
        blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Imagen"
        verbose_name = "Imagenes"
