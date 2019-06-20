
from django.db import models



# Modelo de los Servicios
class Servicio (models.Model):
	codSer = models.CharField(max_length = 10, primary_key = True)
	nomSer = models.CharField(max_length = 200) # Nombre del servicio
	precio = models.DecimalField(max_digits = 3, decimal_places = 2)
	duraci = models.IntegerField()# Duracion PROMEDIO del servicio en minutos

	def __str__(self):
		return self.nomSer
	
	class Meta:
		ordering = ('codSer',)


# Modelo de laas citas.
class Cita (models.Model):
	numCit = models.IntegerField(primary_key = True)# Numero de cita del dia
	nomPac = models.CharField(max_length = 255, help_text = "Ingrese los nombres, solo letras")
	apePac = models.CharField(max_length = 255, help_text = "Ingrese los apellidos, solo letras")
	telPac = models.IntegerField(unique = True, help_text = "Solo numeros")# Telefono del paciente
	fecCon = models.DateField(help_text = "Seleccione la fecha para la cita")# Fecha de la consulta
	horCon = models.CharField(max_length = 10, null=True, help_text="Seleccione un horario disponible")
	fecCre = models.DateField(auto_now_add = True)# afecha de creacion

	class Meta:
		ordering = ('numCit',)

# Relacion de Muchos a Muchos entre Cita y Servicio
class CitaServicio(models.Model):
	cita = models.ForeignKey(Cita, on_delete = models.PROTECT )
	servicio = models.ForeignKey(Servicio, on_delete = models.PROTECT)


# Create your models here.
class Medicamento(models.Model):
	codMedicamento=models.IntegerField(help_text="Ingrese el codigo del Medicamento",primary_key = True)
	nomMedicamento=models.CharField(max_length=200,help_text="Ingrese el nombre del Medicamento")
	def __str__(self):
		return self.nomMedicamento

class Medico(models.Model):
	codMedico=models.IntegerField(help_text="Ingrese el codigo del Medico",primary_key = True)
	nomMedico=models.CharField(max_length=200,help_text="Ingrese el nombre del Medico")
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nomMedico

class Secretaria(models.Model):
	codSec=models.IntegerField(help_text="Ingrese el codigo de la Secretaria",primary_key = True)
	nomSec=models.CharField(max_length=200,help_text="Ingrese el nombre de la Secretaria")
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nomSec

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

	def __str__(self):
		 return '{0}, {1}'.format(self.codUsu, self.pasUsu)


class Consulta(models.Model):
	codCon=models.IntegerField(primary_key = True)
	diagnostico=models.CharField(max_length=500,help_text="Ingrese el diagnostico")
	dosis=models.CharField(max_length=500,help_text="Ingrese la dosis")
	#paciente = models.ManyToManyField(Paciente, help_text="Seleccione el paciente")
	medico=models.ForeignKey('Medico', on_delete=models.SET_NULL, null=True)
	medicamentos=models.ManyToManyField(Medicamento)
	servicios=models.ManyToManyField(Servicio)
	def __str__(self):
		return self.codCon