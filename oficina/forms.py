from django import forms
from .models import *


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['status_o', 'o_client', 'o_product', 'o_payment', 's_price']  # Inclua todos os campos necessários

    status_o = forms.ChoiceField(choices=Orders.Order_Status_Choices.choices, required=True, label="Status da Ordem")
    o_client = forms.ModelChoiceField(queryset=Clients.objects.all(), required=True, label="Cliente")
    o_product = forms.ModelChoiceField(queryset=Products.objects.all(), required=True, label="Produto")
    o_payment = forms.ModelChoiceField(queryset=Payments.objects.all(), required=True, label="Forma de Pagamento")
    s_price = forms.ModelChoiceField(queryset=Services.objects.all(), required=True, label="Serviço")

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email', 'addres', 'cpf', 'rg', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'addres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'status_p', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'status_p': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Produto', 'rows': 3}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return name


class ServicesForm(forms.ModelForm):  # Novo formulário para o modelo Services
    class Meta:
        model = Services
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Serviço'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Serviço', 'rows': 3}),
        }
