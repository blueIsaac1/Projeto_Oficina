import os
import django
import random
from faker import Faker

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectOficina.settings')  # Altere 'SeuProjeto' para o nome do seu projeto
django.setup()

from oficina.models import Services, Categories, Clients, Products, Payments, Orders, Employee

fake = Faker()

def insert_data():
    # Inserir dados em Services
    # for _ in range(15):
    #     service = Services(name=fake.word().capitalize(), price=round(random.uniform(10.0, 500.0), 2), 
    #                        description=fake.sentence())
    #     service.save()

    # # Inserir dados em Categories
    # for _ in range(10):
    #     category = Categories(name=fake.word().capitalize(), description=fake.sentence())
    #     category.save()

    # Inserir dados em Clients
    for _ in range(15):
        client = Clients(
            name=fake.name(),
            email=fake.unique.email(),
            addres=fake.address(),
            cpf=fake.unique.random_int(min=10000000000, max=99999999999), 
            rg=fake.unique.random_int(min=100000000, max=999999999), 
            phone=fake.unique.phone_number()[:11]  # Assegura que o telefone não exceda 11 caracteres
        )
        client.save()

    # Inserir dados em Products
    categories = Categories.objects.all()  # Pegando todas as categorias
    for _ in range(15):
        product = Products(
            name=fake.word().capitalize(),
            status_p=random.choice(['1', '2']), 
            category=random.choice(categories), 
            description=fake.sentence()
        )
        product.save()

    # Inserir dados em Payments
    for _ in range(20):
        payment = Payments(method=random.choice(['1', '2', '3', '4', '5']))  # Escolhendo aleatoriamente o método de pagamento
        payment.save()

    # Inserir dados em Orders
    clients = Clients.objects.all()
    products = Products.objects.all()
    payments = Payments.objects.all()
    services = Services.objects.all()
    for _ in range(15):
        order = Orders(
            status_o=random.choice(['1', '2', '3', '4']), 
            o_client=random.choice(clients), 
            o_product=random.choice(products), 
            o_payment=random.choice(payments),
            created_by=None, 
            s_price=random.choice(services)
        )
        order.save()

    # Inserir dados em Employee
    for _ in range(10):
        employee = Employee(
            e_name=fake.name(),
            e_email=fake.unique.email(),
            e_addres=fake.address(),
            e_cpf=fake.unique.random_int(min=10000000000, max=99999999999), 
            e_rg=fake.unique.random_int(min=100000000, max=999999999), 
            e_phone=fake.unique.phone_number()[:11]  # Assegura que o telefone não exceda 11 caracteres
        )
        employee.save()

    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    insert_data()
