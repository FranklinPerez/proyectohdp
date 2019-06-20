
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'nomPac', 'apePac', 'telPac', 'fecCon', 'horCon',
		}
		labels ={
			'nomPac': 'Nombres ','apePac': 'Apellidos ','telPac': 'Telefono ','fecCon': 'Fecha de Consulta ','horCon': 'Hora de Consulta ',
		}

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = {
			'nomSer', 'precio', 'duraci',
		}
		labels ={
			'nomSer': 'Nombre del Servicio ','precio': 'Precio ($) ','duraci': 'Duracion ',
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

