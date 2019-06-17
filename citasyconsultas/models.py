from django.db import models

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
	codServicio=models.CharField(
		max_length=10,
		help_text="Ingrese el codigo del Servicio"
		)
	nomServicio=models.CharField(
		max_length=200,
		help_text="Ingrese el nombre del Servicio"
		)
	preServicio=models.DecimalField(
		max_digits=5,
		decimal_places=2,
		help_text="Ingrese el precio del Servicio"
		)
	def __str__(self):
		 return '{0}, {1}'.format(self.nomServicio, self.preServicio)