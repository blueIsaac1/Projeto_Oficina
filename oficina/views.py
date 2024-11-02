from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *

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
    form_order = OrdersForm()
    form_client = ClientForm()
    form_product = ProductsForm()
    form_type = request.POST.get('form_type')
    #####
    orders_starteds = Orders.objects.filter(status_o = 1)
    orders_in_progress = Orders.objects.filter(status_o = 2)
    orders_completed = Orders.objects.filter(status_o = 3)

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('new_status')
        if order_id and new_status:
            try:
                order = Orders.objects.get(id=order_id)
                order.status_o = new_status
                order.save()
                return JsonResponse({'success': True})  # Retorna uma resposta JSON de sucesso
            except Orders.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Order not found.'})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})

    if form_type == 'order_form':
        form_order = OrdersForm(request.POST)
        if form_order.is_valid():
            form_order.save()
            return redirect(organizador)
        
    if form_type == 'client_form':
        form_client = ClientForm(request.POST)
        if form_client.is_valid():
            form_client.save()
            return redirect(organizador)
        
    if form_type == 'product_form':
        form_product = ProductsForm(request.POST)
        if form_product.is_valid():
            form_product.save()
            return redirect(organizador)

    return render(request, 'oficina/organizador.html', context={
        'os': orders_starteds,
        'op': orders_in_progress,
        'oc': orders_completed,
        'form_order': form_order,
        'form_client': form_client,
        'form_product': form_product
    })

