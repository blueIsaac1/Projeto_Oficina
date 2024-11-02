from django import forms
from .models import *

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['status_o', 'o_client', 'o_product', 'o_payment', 'price']  # Inclua os campos que deseja exibir no formulário

    # Campo personalizado para status com base nas opções do modelo
    status_o = forms.ChoiceField(choices=Orders.Order_Status_Choices.choices, required=True)
    
    # Exemplo de um campo de seleção de cliente, produto e pagamento
    o_client = forms.ModelChoiceField(queryset=Clients.objects.all(), required=True, label="Cliente")
    o_product = forms.ModelChoiceField(queryset=Products.objects.filter(orders__isnull=True), required=True, label="Produto")
    o_payment = forms.ModelChoiceField(queryset=Payments.objects.all(), required=True, label="Forma de Pagamento")

    # Exemplo de um campo para o preço
    # Corrigir Erro
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label="Preço")

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email', 'addres', 'cpf', 'rg', 'phone']  # Campos a serem incluídos no formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'addres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }
        
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11:
            raise forms.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf

    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if len(rg) != 9:
            raise forms.ValidationError("O RG deve ter 9 dígitos.")
        return rg

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 11:
            raise forms.ValidationError("O telefone deve ter 11 dígitos.")
        return phone
    
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'status_p', 'category', 'description']  # Campos a serem incluídos no formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'status_p': forms.Select(attrs={'class': 'form-control'}),  # Para seleção de status
            'category': forms.Select(attrs={'class': 'form-control'}),  # Para seleção da categoria
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Produto', 'rows': 3}),
        }
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return name