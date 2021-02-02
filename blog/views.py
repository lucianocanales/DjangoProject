from django.shortcuts import render
from blog.models import Post, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post(request, post_id):

    entrada = Post.objects.get(id=post_id)
    category = entrada.categorias.all()
    contexto = {
        'post': entrada,
        'categorias': category,
    }
    return render(request, 'blog/post.html', contexto)


def blog(request):
    entradas = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(entradas, 12)
    try:
        entradas = paginator.page(page)
    except PageNotAnInteger:
        entradas = paginator.page(1)
    except EmptyPage:
        entradas = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog.html', {'entradas': entradas})


def category(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    entradas = Post.objects.filter(categorias=categoria)
    return render(
        request,
        'blog/categoria.html',
        {
            'categoria': categoria,
            'entradas': entradas
        }
    )


def categorias(request):
    Categoria = categoria.objects.all()
    return render(request, 'blog/categorias.html', {'categorias': Categoria})
