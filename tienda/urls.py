from django.urls import path
from tienda import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('producto/<producto_id>/', views.producto, name='producto'),

]
