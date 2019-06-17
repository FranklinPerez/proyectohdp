

from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Cita, CitaServicio



class CrearCita(CreateView):
	model = Cita
	fields =[
		'nomPac',
		'apePac',
		'telPac',
		'fecCon',
	]

