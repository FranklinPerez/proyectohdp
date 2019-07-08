
from django.core.exceptions import ValidationError

def valid_Nombres(value):
	
	letras = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú";

	for i in value:
		if i not in letras:
			raise ValidationError('Este no es un nombre valido')

def valid_Apellidos(apellido):

	letras = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú";

	for i in apellido:
		if i not in letras:
			raise ValidationError('Este no es un apellido valido')

def valid_Telefono(tel):

	numeros = "0123456789";

	for i in tel:
		if i not in numeros:
			raise ValidationError('Solo se permiten numeros')
