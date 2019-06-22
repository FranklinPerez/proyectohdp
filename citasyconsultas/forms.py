
from django.forms.widgets import SelectDateWidget 
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'numCit', 'pacien', 'fecCon', 'horCon', 'servic',#'estado',
		}
		labels = {
			'numCit': 'Número de Cita           ',
			'pacien': 'Paciente                 ',
			'fecCon': 'Fecha de Consulta        ',
			'horCon': 'Hora de Consulta         ',
			'servic': 'Motivo de Consulta       ',
			#'estado': 'Estado de la Cita'
		}
		#fecCon = forms.DateField(widget = SelectDateWidget)


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
			"numExpediente", "nomPaciente", "apelPaciente", "fechaNacimiento", "emailPaciente", "telefono",
		}
		labels = {
			"numExpediente" : "Número de expediente: ", "nomPaciente" : "Nombre del paciente: ",
			"apelPaciente" : "Apellido del paciente: ", "fechaNacimiento" : "Fecha de nacimiento: ",
			"emailPaciente" : "eMail: ", "telefono" : "Teléfono de contacto: ",
		}