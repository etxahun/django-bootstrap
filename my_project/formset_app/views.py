# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from formset_app.models import *
from formset_app.forms import *

def formset(request):
    form = MetaPokemonForm(prefix = 'pokemon_fs')
    attack_formset = AttackFormSet(instance = Pokemon(), prefix = 'attack_fs')
    type_formset = TypeFormSet(instance = Pokemon(), prefix = 'type_fs')

    if request.POST:
        form = MetaPokemonForm(request.POST, prefix = 'pokemon_fs')
        if form.is_valid():
            cd_p = form.cleaned_data

            print "2"
            pokemon = form.save(commit = False)
            attack_formset = AttackFormSet(request.POST, instance = pokemon, prefix = 'attack_fs')
            type_formset = TypeFormSet(request.POST, instance = pokemon, prefix = 'type_fs')

            # Do whatever with the cleaned data from the pokemon form

            pokemon.name = cd_p['name']
            pokemon.description = cd_p['description']
            pokemon.number = cd_p['number']
            pokemon.weight = cd_p['weight']
            pokemon.height = cd_p['height']
            pokemon.generation = cd_p['generation']

            pokemon.save()

            if attack_formset.is_valid():
                for form_a in attack_formset:
                    if (len(form_a.cleaned_data) > 0):

                        # Do whatever with the cleaned data from each attack form

                        form_a.save()
                    else:
                        print "No attacks to save"

                attack_formset.save()

            if type_formset.is_valid():
                for form_t in type_formset:
                    if (len(form_t.cleaned_data) > 0):

                        # Do whatever with the cleaned data from each type form

                        form_t.save()
                    else:
                        print "No types to save"

                type_formset.save()

            return HttpResponseRedirect("/added")
    else:
        form = MetaPokemonForm(prefix = 'pokemon_fs')
        attack_formset = AttackFormSet(instance = Pokemon(), prefix = 'attack_fs')
        type_formset = TypeFormSet(instance = Pokemon(), prefix = 'type_fs')

    return render_to_response("formset_app/formset.html", {
            "form": form,
            "attack_formset": attack_formset,
            "type_formset": type_formset,
        }, context_instance = RequestContext(request))


def added(request):
    return render_to_response('added.html')
