from django.db import models
from django.contrib.auth.models import User


class Services(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.price}"


class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"Categoria: {self.name}"


class Clients(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    addres = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.name}"


class Products(models.Model):
    name = models.CharField(max_length=50)

    class ProductStatusChoices(models.TextChoices):
        ACTIVE = '1', 'Ativo'
        INACTIVE = '2', 'Inativo'

    status_p = models.CharField(max_length=1, choices=ProductStatusChoices.choices, default=ProductStatusChoices.ACTIVE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Payments(models.Model):
    class PaymentMethodChoices(models.TextChoices):
        PIX = '1', 'Pix'
        DEBIT = '2', 'Débito'
        CREDIT = '3', 'Crédito'
        CASH = '4', 'Dinheiro'
        NULL = '5', 'Nulo'

    method = models.CharField(max_length=1, choices=PaymentMethodChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_method_display()}"


class Orders(models.Model):
    class Order_Status_Choices(models.TextChoices):
        STARTED = '1', 'Iniciado'
        IN_PROGRESS = '2', 'Em andamento'
        COMPLETED = '3', 'Finalizado'
        CANCELED = '4', 'Cancelado'

    status_o = models.CharField(max_length=1, choices=Order_Status_Choices.choices, default=Order_Status_Choices.STARTED)
    o_client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    o_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='orders')
    o_payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    s_price = models.ForeignKey(Services, on_delete=models.CASCADE)  # s_price linked to Services model
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')

    def __str__(self):
        return f"Ordem {self.id} - Cliente: {self.o_client} - Produto: {self.o_product}"


class Employee(models.Model):
    e_name = models.CharField(max_length=100)
    e_email = models.CharField(max_length=50, unique=True)
    e_addres = models.CharField(max_length=150)
    e_cpf = models.CharField(max_length=11, unique=True)
    e_rg = models.CharField(max_length=9, unique=True)
    e_phone = models.CharField(max_length=11, unique=True)
    e_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Funcionario: {self.e_name}"
