from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def oficina(request):
    return render(request, 'oficina/main.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # ou qualquer página de destino após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'Oficina/login.html')

def organizador(request):
    return render(request, 'oficina/organizador.html')


