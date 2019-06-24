
from django import forms
from .models import *


		
class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'numCit', 'pacien', 'fecCon', 'horCon', 'servic',
		}
		labels = {
			'numCit': 'Número de Cita',
			'pacien': 'Paciente ',
			'fecCon': 'Fecha de Cita',
			'horCon': 'Hora ',
			'servic': 'Motivo de la Cita ',
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
		widgets ={
			'fechaNacimiento' : forms.DateInput(attrs={'class':'datepicker'}),
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


class ModificarCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'pacien', 'fecCon', 'horCon', 'servic','estado',
		}
		labels = {
			
			'pacien': 'Paciente ',
			'fecCon': 'Fecha de Cita',
			'horCon': 'Hora ',
			'servic': 'Motivo de la Cita ',
			'estado': 'Estado ( 0-> Activa, 1-> Finalizada)'
		}
		widgets ={
			'fecCon' : forms.DateInput(attrs={'class':'datepicker'}),
		}
