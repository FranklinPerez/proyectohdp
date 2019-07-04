
from django.core.exceptions import ValidationError

def valid_Nombres(value):
	
	letras = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú";

	for i in value:
		if i not in letras:
			raise ValidationError('No se permiten numeros en los nombres')

def valid_Apellidos(apellido):

	letras = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú";

	for i in apellido:
		if i not in letras:
			raise ValidationError('No se permiten numeros en los apellidos')

def valid_Telefono(tel):

	numeros = "0123456789";

	for i in tel:
		if i not in numeros:
			raise ValidationError('No es un numero telefonico valido')