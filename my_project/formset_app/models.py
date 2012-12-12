# coding: utf-8

from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Pokemon(models.Model):
	name = models.CharField(
		max_length = 25,
		verbose_name = 'Nombre'
	)
	description = models.TextField(
		max_length = 500,
		verbose_name = 'Descripción'
	)
	number = models.IntegerField(
		validators = [MinValueValidator(1), MaxValueValidator(649)],
		verbose_name = 'Número Pokédex'
	)
	weight = models.DecimalField(
		max_digits = 5,
		decimal_places = 2,
		verbose_name = 'Peso'
	)
	height = models.DecimalField(
		max_digits = 4,
		decimal_places = 2,
		verbose_name = 'Altura'
	)
	generation = models.IntegerField(
		validators = [MinValueValidator(1), MaxValueValidator(5)],
		verbose_name = 'Generación'
	)

class Attack(models.Model):
	pokemon = models.ForeignKey(Pokemon)
	attack_name = models.CharField(
		max_length = 25,
		verbose_name = 'Ataque'
	)
	learning_level = models.IntegerField(
		validators = [MinValueValidator(1), MaxValueValidator(100)],
		verbose_name = 'Nivel'
	)

class Type(models.Model):
	pokemon = models.ForeignKey(Pokemon)
	pokemon_type = models.CharField(
		max_length = 25,
		verbose_name = 'Tipo'
	)
