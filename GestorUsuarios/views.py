from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileForm


# Create your views here.


class ProfileView(ListView):
    model = Profile
    template_name = 'GestionUsuarios/profile.html'


class SegurityView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'GestionUsuarios/seguridad.html'


class Login(LoginView):
    template_name = 'GestionUsuarios/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
