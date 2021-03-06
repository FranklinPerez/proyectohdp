from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from .models import *




		
class NuevaCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = (
			'numCit', 'pacien', 'servic', 'fecCon', 'horCon', 
		)
		labels = {
			'numCit': 'Número de Cita',
			'pacien': 'Paciente',
			'servic': 'Motivo de la Cita',
			'fecCon': 'Fecha de Cita',
			'horCon': 'Hora',
		}
		widgets ={
			'fecCon' : forms.DateInput(attrs={'class':'datepicker'}),
		}


class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = (
			'codSer', 'nomSer','precio','duraci',
		)
		labels = {
			'codSer':'Codigo',
		    'nomSer':'Nombre',
		    'precio':'Precio ($)',
		    'duraci':'Duracion (Min.)',
		}	


class MedicamentoForm(forms.ModelForm):
	class Meta:
		model=Medicamento
		fields=(
		'codMedicamento', 'nomMedicamento',
		)
		labels={
		'codMedicamento':'Codigo del Medicamento', 'nomMedicamento':'nombre del Medicamento',
		}		

class ExpedienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = (
			'numExpediente', 'nomPaciente', 'apelPaciente', 'fechaNacimiento', 'emailPaciente',
			 'depResidencia', 'munResidencia', 'telefono',
		)
		labels = {
			'numExpediente' : 'Número de expediente', 'nomPaciente' : 'Nombre',
			'apelPaciente' : 'Apellido', 'fechaNacimiento' : 'Fecha de nacimiento',
			'emailPaciente' : 'eMail', 'depResidencia' : 'Departamento', 'munResidencia' : 'Municipio', 
			'telefono' : 'Teléfono',
		}
		widgets ={
			'fechaNacimiento' : forms.DateInput(attrs={'class':'datepicker'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['munResidencia'].queryset = Municipio.objects.none()
		if 'depResidencia' in self.data:
			try:
				departamento_id = int(self.data.get('depResidencia'))
				self.fields['munResidencia'].queryset = Municipio.objects.filter(departamento_id=departamento_id)
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['munResidencia'].queryset = self.instance.departamento.municipio_set
  


class ConsultaForm(forms.ModelForm):
	class Meta:
		model=Consulta
		fields=(
		'paciente', 'servicios','diagnostico','dosis','medicamentos','estado',
		)
		labels={
		'paciente':'Paciente', 'servicios':'Servicio que se aplico','diagnostico':'diagnostico','dosis':'dosis','medicamentos':'medicamentos recetados','estado':'colocar 1 para terminar consulta',
		}
# VISTAS ESPECIALES PARA MODIFICAR====================================0
class ModificarCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = (
			'pacien', 'fecCon', 'horCon', 'servic','estado',
		)
		labels = {

			'pacien': 'Paciente ',
			'fecCon': 'Fecha de Cita',
			'horCon': 'Hora ',
			'servic': 'Motivo de la Cita ',
			'estado': 'Estado'
		}
		widgets ={
			'fecCon' : forms.DateInput(attrs={'class':'datepicker'}),
		}
		
class ModificarServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = (
			'nomSer','precio','duraci',
		)
		labels = {
		    'nomSer':'Nombre',
		    'precio':'Precio ($)',
		    'duraci':'Duracion (Min.)',
		}	

class ModificarExpedienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = (
			'nomPaciente', 'apelPaciente', 'fechaNacimiento', 'emailPaciente',
			'depResidencia', 'munResidencia', 'telefono',
		)
		labels = {
			"nomPaciente" : "Nombre del paciente ",
			"apelPaciente" : "Apellido del paciente ", "fechaNacimiento" : "Fecha de nacimiento ",
			"emailPaciente" : "e-Mail", "depResidencia" : "Departamento", "munResidencia" : "Municipio", 
			"telefono" : "Teléfono de contacto ",
		}
		widgets ={
			'fechaNacimiento' : forms.DateInput(attrs={'class':'datepicker'}),
		}

#===================================================================================

class nuevaConsultaForm(forms.ModelForm):
	class Meta:
		model=Consulta
		fields=(
		'paciente', 'servicios',
		)
		labels={
		'paciente':'Paciente', 'servicios':'Motivo de la consulta',
		}

class UsuarioForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = Usuario
		fields=('codUsu', 'pasUsu')

