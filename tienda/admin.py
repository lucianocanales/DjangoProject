from django.contrib import admin
from .models import Categoria, ImagenProducto
from .models import Imagen, Producto, Caracteristica
from .models import ImageCarousel
# Register your models here.


class ImageCarouselAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto


class CaracteristicaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ImagenProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    inlines = [
        ImagenProductoInline,
    ]


class ImagenesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    inlines = [
        ImagenProductoInline,
    ]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Imagen, ImagenesAdmin)
admin.site.register(ImagenProducto, ImagenProductoAdmin)
admin.site.register(ImageCarousel, ImageCarouselAdmin)
