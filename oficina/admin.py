from django.contrib import admin
from .models import Categories, Clients, Products, Payments, Orders, Employee

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'phone', 'created_at')
    search_fields = ('name', 'cpf', 'email')
    list_filter = ('created_at',)
    fieldsets = (
        ('Informações Pessoais', {'fields': ('name', 'email', 'addres')}),
        ('Documentos', {'fields': ('cpf', 'rg')}),
        ('Contato', {'fields': ('phone',)}),
    )

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status_p', 'category', 'description')
    list_filter = ('status_p', 'category')
    search_fields = ('name',)

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'created_at')
    list_filter = ('method',)

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_o', 'o_client', 'o_product', 'o_payment', 'price', 'created_by', 'created_at')
    list_filter = ('status_o', 'created_at', 'created_by')
    search_fields = ('o_client__name', 'o_product__name')
    fieldsets = (
        ('Informações do Pedido', {'fields': ('status_o', 'price')}),
        ('Cliente e Produto', {'fields': ('o_client', 'o_product')}),
        ('Pagamento', {'fields': ('o_payment',)}),
        ('Informações Adicionais', {'fields': ('created_by',)}),
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'e_name', 'e_email', 'e_cpf', 'e_phone', 'e_created_at')
    search_fields = ('e_name', 'e_cpf', 'e_email')
    list_filter = ('e_created_at',)
    fieldsets = (
        ('Informações Pessoais', {'fields': ('e_name', 'e_email', 'e_addres')}),
        ('Documentos', {'fields': ('e_cpf', 'e_rg')}),
        ('Contato', {'fields': ('e_phone',)}),
    )
