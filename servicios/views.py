from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def servicios(request):
    Servicios=Servicio.objects.all()
    return render(request,'servicios/servicios.html',{'servicios':Servicios})