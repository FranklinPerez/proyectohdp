
from django import forms
from .models import *

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = {
			'nomPac', 'apePac', 'telPac', 'fecCon',
		}
		labels ={
			'nomPac': 'Nombres ','apePac': 'Apellidos ','telPac': 'Telefono ','fecCon': 'Fecha de Consulta ',
		}

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = {
			'nomSer', 'precio', 'duraci',
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

