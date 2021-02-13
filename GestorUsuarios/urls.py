from django.urls import path
from GestorUsuarios import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='loguot'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('seguridad/', views.SegurityView.as_view(), name='seguridad'),

]
