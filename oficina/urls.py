from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.oficina, name='home'),
    path('', views.login, name='login'),
    path('organizador/', views.organizador, name='organizador'),

]