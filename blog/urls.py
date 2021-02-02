from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<categoria_id>/', views.category, name='categoria'),
    path('post/<post_id>/', views.post, name='post'),
    path('categorias/', views.categorias, name='categorias')
]
