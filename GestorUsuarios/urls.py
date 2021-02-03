from django.urls import path
from GestorUsuarios import views

urlpatterns = [
    path('', views.Login.as_view(), name='Login'),

]
