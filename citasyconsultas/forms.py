<<<<<<< HEAD

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
=======
from django import forms
from .models import *


class MedicamentoForm(forms.ModelForm):
	class Meta:
		model=Medicamento
		fields={
		'codMedicamento', 'nomMedicamento',
		}
		labels={
		'codMedicamento':'Codigo del Medicamento', 'nomMedicamento':'nombre del Medicamento',
		}		
>>>>>>> e61d06ba1b655322d1ce9f18c9daa07f775672c8
