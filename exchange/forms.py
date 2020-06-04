from django import forms
from .models import *
from django.core.exceptions import ValidationError


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['title', 'cod1c7', 'sql_base', 'tr5_path', 'sql_server', 'region']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cod1c7': forms.TextInput(attrs={'class': 'form-control'}),
            'sql_base': forms.TextInput(attrs={'class': 'form-control'}),
            'tr5_path': forms.TextInput(attrs={'class': 'form-control'}),
            'sql_server': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'region': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
