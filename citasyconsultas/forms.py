
from django import forms

from .models import Cita, CitaServicio

class NuevaCitaForm(forms.ModelForm):
	class Meta:
		models = Cita
		fields = [
			'Nombre: ',
			'Apellidos: ',
			'Telefono: ',
			'fecCon',
		]