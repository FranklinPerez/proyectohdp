
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'nomPac', 'apePac', 'telPac', 'fecCon', 'horCon', 'servic',
		}
		labels ={
			'nomPac': 'Nombres ',
			'apePac': 'Apellidos ',
			'telPac': 'Telefono ',
			'fecCon': 'Fecha de Consulta ',
			'horCon': 'Hora de Consulta ',
			'servic': 'Motivo de Consulta',
		}

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = {
			'nomSer', 'precio', 'duraci',
		}
		labels ={
			'nomSer': 'Nombre del Servicio ','precio': 'Precio ($) ','duraci': 'Duracion (Min) ',
		}

class MedicamentoForm(forms.ModelForm):
	class Meta:
		model=Medicamento
		fields={
		'codMedicamento', 'nomMedicamento',
		}
		labels={
		'codMedicamento':'Codigo del Medicamento', 'nomMedicamento':'nombre del Medicamento',
		}		

class ExpedienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = {
			"numExpediente", "nomPaciente", "apelPaciente", "fechaNacimiento", "emailPaciente",
			 "depResidencia", "munResidencia", "telefono",
		}
		labels = {
			"numExpediente" : "Número de expediente: ", "nomPaciente" : "Nombre del paciente: ",
			"apelPaciente" : "Apellido del paciente: ", "fechaNacimiento" : "Fecha de nacimiento: ",
			"emailPaciente" : "eMail: ", "depResidencia" : "Departamento: ", "munResidencia" : "Municipio: ", 
			"telefono" : "Teléfono de contacto: ",
		}

class ServicioForm(forms.ModelForm):
	class Meta:
		model=Servicio
		fields={
		'codSer', 'nomSer','precio','duraci',
		}
		labels={
		'codSer':'Codigo del Servicio', 'nomSer':'nombre del Servicio','precio':'Precio del Servicio','duraci':'Duracion del Servicio (en minutos)',
		}