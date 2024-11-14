from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'Oficina/login.html')


def oficina(request):
    form_order = OrdersForm()
    form_client = ClientForm()
    form_product = ProductsForm()
    form_type = request.POST.get('form_type')

    orders_starteds = Orders.objects.filter(status_o=1)
    orders_in_progress = Orders.objects.filter(status_o=2)
    orders_completed = Orders.objects.filter(status_o=3)

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
            return redirect(oficina)

    if form_type == 'client_form':
        form_client = ClientForm(request.POST)
        if form_client.is_valid():
            form_client.save()
            return redirect(oficina)

    if form_type == 'product_form':
        form_product = ProductsForm(request.POST)
        if form_product.is_valid():
            form_product.save()
            return redirect(oficina)

    return render(request, 'Oficina/main.html', context={
        'os': orders_starteds,
        'op': orders_in_progress,
        'oc': orders_completed,
        'form_order': form_order,
        'form_client': form_client,
        'form_product': form_product
    })


def formulario(request):
    form_order = OrdersForm()
    form_client = ClientForm()
    form_service = ServicesForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Processa o formulário de ordem e salva no banco de dados
        if form_type == 'order_form':
            form_order = OrdersForm(request.POST)
            if form_order.is_valid():
                form_order.save()  # Salva a nova ordem
                return redirect('formulario')

        elif form_type == 'client_form':
            form_client = ClientForm(request.POST)
            if form_client.is_valid():
                form_client.save()
                return redirect('formulario')

        elif form_type == 'service_form':
            form_service = ServicesForm(request.POST)
            if form_service.is_valid():
                form_service.save()
                return redirect('formulario')

    context = {
        'form_order': form_order,
        'form_client': form_client,
        'form_service': form_service,
    }

    return render(request, 'Oficina/formulario.html', context)

# @csrf_exempt
# def update_status(request):
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')
#         new_status = request.POST.get('new_status')
#         if order_id and new_status:
#             # Verifique e atualize o status do produto
#             try:
#                 product = Orders.objects.get(id=order_id)
#                 product.status = new_status
#                 product.save()
#                 return JsonResponse({'success': True, 'status': product.status})
#             except Orders.DoesNotExist:
#                 return JsonResponse({'success': False, 'error': 'Produto não encontrado'})
#     return JsonResponse({'success': False, 'error': 'Método inválido'})