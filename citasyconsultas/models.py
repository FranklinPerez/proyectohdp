
from django.db import models

<<<<<<< HEAD

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
	fecCon = models.DateTimeField(help_text = "Seleccione una fecha para la cita")# Fecha de la consulta
	fecCre = models.DateField(auto_now_add = True)# afecha de creacion

	class Meta:
		ordering = ('numCit',)

# Relacion de Muchos a Muchos entre Cita y Servicio
class CitaServicio(models.Model):
	cita = models.ForeignKey(Cita, on_delete = models.PROTECT )
	servicio = models.ForeignKey(Servicio, on_delete = models.PROTECT)





=======
# Create your models here.
class Medicamento(models.Model):
	codMedicamento=models.CharField(
		max_length=10,
		help_text="Ingrese el codigo del Medicamento"
		)
	nomMededicamento=models.CharField(
		max_length=200,
		help_text="Ingrese el nombre del Medicamento"
		)
	def __str__(self):
		return self.nomMeddicamento

class Medico(models.Model):
	codMedico=models.CharField(
		max_length=10,
		help_text="Ingrese el codigo del Medico"
		)
	nomMedico=models.CharField(
		max_length=200,
		help_text="Ingrese el nombre del Medico"
		)
	def __str__(self):
		return self.nomMedico

class Servicio(models.Model):
	codSer=models.CharField(
		max_length=10,
		help_text="Ingrese el codigo del Servicio"
		)
	nomSer=models.CharField(
		max_length=200,
		help_text="Ingrese el nombre del Servicio"
		)
	preSer=models.DecimalField(
		max_digits=5,
		decimal_places=2,
		help_text="Ingrese el precio del Servicio"
		)
	def __str__(self):
		 return '{0}, {1}'.format(self.nomSer, self.preSer)
>>>>>>> b4ca0ebcdf8fbe2b519dce899922db8e11b985c3
