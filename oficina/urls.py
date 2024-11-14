from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main/', views.oficina, name='home'),
    path('formulario/', views.formulario, name='formulario'),
    # path('update_status/', views.update_status, name='update_status'),

]