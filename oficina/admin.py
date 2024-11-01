from django.contrib import admin
from .models import Categories, Clients, Products, Payments, Orders, Employee

admin.site.register(Categories)
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Payments)
admin.site.register(Orders)
admin.site.register(Employee)
