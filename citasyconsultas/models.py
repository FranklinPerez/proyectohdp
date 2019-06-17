from django.db import models

# Create your models here.
class Medicamento(models.Model):
	codMedicamento=models.CharField(max_length=10,help_text="Ingrese el codigo del Medicamento",primary_key = True)
	nomMedicamento=models.CharField(max_length=200,help_text="Ingrese el nombre del Medicamento")
	def __str__(self):
		return self.nomMedicamento

class Medico(models.Model):
	codMedico=models.CharField(max_length=10,help_text="Ingrese el codigo del Medico",primary_key = True)
	nomMedico=models.CharField(max_length=200,help_text="Ingrese el nombre del Medico")
	def __str__(self):
		return self.nomMedico

class Servicio(models.Model):
	codSer=models.CharField(max_length=10, primary_key = True)
	nomSer=models.CharField(max_length=200)# Nombre del servicio
	preSer=models.DecimalField(max_digits=3, decimal_places=2)
	duraci=models.DurationField()#Duracion PROMEDIO del servicio

	class Meta:
		ordering=['codSer','preSer']

	def __str__(self):
		 return '{0}, {1}'.format(self.nomSer, self.preSer)

	

class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (
		('s','Secretaria'),
		('m', 'Medico'),		
		)

	tipo_usuario= models.CharField(
        max_length=1,
        choices=TIPO_USUARIO,
        blank=True,
        default='s',
        help_text='Tipo de usuario en el sistema')
		