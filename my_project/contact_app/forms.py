# -*- coding: utf-8 -*-

# Create your forms here.

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(attrs = {'class': 'input-xlarge'}),
        required = True,
        label = 'Nombre'
    )
    email = forms.EmailField(
        widget = forms.TextInput(attrs = {'class': 'input-xlarge', 'placeholder': 'email@example.com'}),
        required = True,
        label = 'E-mail'
    )
    subject = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(attrs = {'class': 'input-xlarge'}),
        required = True,
        label = 'Asunto'
    )
    message = forms.CharField(
        widget = forms.Textarea(attrs = {'class': 'input-xlarge', 'rows': '5'}),
        required = False,
        label = 'Mensaje'
    )
