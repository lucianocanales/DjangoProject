from django.shortcuts import render
from .models import ImagenProducto, Categoria, Producto
from .models import ImageCarousel
from PIL import Image

# Create your views here.


def tienda(request):
    entradas = ImagenProducto.objects.all()
    caracteristic = Producto.objects.all()
    images_carousel = ImageCarousel.objects.all()
    return render(
        request,
        "tienda/tienda.html",
        {
            "imagenes": entradas,
            "caracteristicas": caracteristic,
            "images_carousel": images_carousel,
        },
    )


def producto(request, producto_id):
    """
    Carga la vista productos levanta de la DB los datos de los productos e
    imagenes de los mismos, y las ajusta a 350x350 guardando una imagen con un
    nuevo tama;o
    """

    producto = Producto.objects.get(id=producto_id)
    category = Producto.objects.get(id=producto_id).categorias
    recomenda = Producto.objects.filter(
        categorias=category).exclude(id=producto_id)
    imagenes_recomend = ImagenProducto.objects.filter(
        caracteristica__in=recomenda)
    entradas = ImagenProducto.objects.filter(caracteristica=producto)

    # ------- creacion de lista categorias padres --------
    categorias_padres = [category]
    temp = category
    while temp.padre:
        categorias_padres.insert(0, temp.padre)
        temp = temp.padre
    # ---------------- manejo de imagens -----------------
    fondo_med = Image.open("media/imgFondo/fondoImg.jpg")
    fondo_thum = Image.open("media/imgFondo/fondoImgthumbnail.jpg")
    # ajusta las imagenes de entrada para resolucion 350x350 y  100x100
    output_size_med = (350, 350)
    output_size_thum = (100, 100)
    for imagen in entradas:
        # --------------------img thumbnail---------------------
        img_thum = Image.open(imagen.image.imagen.thumbnail)
        fondo_thum = resize(fondo_thum, output_size_thum, img_thum)
        fondo_thum.save(imagen.image.imagen.thumbnail.path)
        fondo_thum = Image.open("media/imgFondo/fondoImgthumbnail.jpg")
        # --------------------img media------------------------
        img_med = Image.open(imagen.image.imagen.medium)
        fondo_med = resize(fondo_med, output_size_med, img_med)
        fondo_med.save(imagen.image.imagen.medium.path)
        fondo_med = Image.open("media/imgFondo/fondoImg.jpg")

    return render(
        request,
        "tienda/producto.html",
        {
            "producto": producto,
            "entradas": entradas,
            "recomendacion": recomenda,
            "imagenes_recomend": imagenes_recomend,
            "categorias_padres": categorias_padres,
        },
    )


def categori(request):
    categoria = Categoria.objects.all()
    return render(request, "tienda/categorias.html", {"categorias": categoria})


def resize(fondo, output_size, img):
    '''
    toma como entrada una objeto imagen de fondo,
    una tupla tipo(x,y) y una imagen y si la imagen
    es menor que el la tupla la centra en el fondo
    creando una imagen de tamaño del fondo debuelve una imagen.
    '''
    if img.height < output_size[0] or img.width < output_size[1]:
        cornerupx = int(output_size[0]/2-img.width/2)
        cornerupy = int(output_size[1]/2-img.height/2)
        box = (cornerupx, cornerupy)
        fondo.paste(img, box)
    else:
        fondo = img
    return fondo
