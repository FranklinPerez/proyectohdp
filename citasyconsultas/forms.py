
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'numCit', 'pacien', 'fecCon', 'horCon', 'servic','estado',
		}
		labels = {
			'numCit': 'Número de Cita',
			'pacien': 'Paciente ',
			'fecCon': 'Fecha de Consulta',
			'horCon': 'Hora de Consulta ',
			'servic': 'Motivo de Consulta',
		}
		widgets ={
			'fecCon' : forms.DateInput(attrs={'class':'datepicker'}),
		}
		


class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = {
			'codSer', 'nomSer','precio','duraci',
		}
		labels = {
			'codSer':'Codigo',
		    'nomSer':'Nombre',
		    'precio':'Precio ($)',
		    'duraci':'Duracion (Min.)',
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

class ConsultaForm(forms.ModelForm):
	class Meta:
		model=Consulta
		fields={
		'paciente', 'servicios','diagnostico','dosis','medicamentos','estado',
		}
		labels={
		'paciente':'Paciente', 'servicios':'Servicio que se aplico','diagnostico':'diagnostico','dosis':'dosis','medicamentos':'medicamentos recetados','estado':'colocar 1 para terminar consulta',
		}