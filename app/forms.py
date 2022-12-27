from django import forms
from .models import CustomerData, OrderDetails
from django.forms import ModelForm


class Signup(ModelForm):
    class Meta:
        model = CustomerData
        labels = {}
        fields = ['name', 'email', 'phone', 'password']
        widgets = {
            'name': forms.TextInput(attrs={}),
            'email': forms.TextInput(attrs={}),
            'phone': forms.TextInput(attrs={}),
            'password': forms.TextInput(attrs={}),
        }


class Login(ModelForm):
    class Meta:
        model = CustomerData
        labels = {}
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={}),
            'password': forms.TextInput(attrs={}),
        }
        



