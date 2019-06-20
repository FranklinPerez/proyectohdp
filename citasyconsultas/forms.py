
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		models = Cita
		fields = {
			'nomPac: ', 'apePac: ', 'telPac: ', 'fecCon',
		}
		labels ={
			'nomPac':'Nombres :','apePac':'Apellidos :','telPac':'Telefono :','fecCon':'Fecha de Consuta :',
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