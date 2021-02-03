from django.shortcuts import render
from django.views.generic import ListView
from .models import ImagesBio

# Create your views here.


class Login(ListView):
    model = ImagesBio
    template_name = 'GestionUsuarios/login.html'
