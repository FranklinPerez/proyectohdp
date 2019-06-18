
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
	fecCon = models.DateTimeField(help_text = "Seleccione una fecha para la cita")# Fecha de la consulta
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
	codMedico=models.IntegerField(max_length=10,help_text="Ingrese el codigo del Medico",primary_key = True)
	nomMedico=models.CharField(max_length=200,help_text="Ingrese el nombre del Medico")
	def __str__(self):
		return self.nomMedico



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

