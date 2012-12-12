# coding: utf-8

from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

# Create your forms here.

from formset_app.models import *

AttackFormSet = inlineformset_factory(Pokemon, Attack, extra = 1)
TypeFormSet = inlineformset_factory(Pokemon, Type, extra = 1)


class MetaPokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
