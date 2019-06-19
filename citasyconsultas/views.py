<<<<<<< HEAD

=======
>>>>>>> b044f7f65bcc261f7ee9bfe1c3fcb2387f211f4a
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *

<<<<<<< HEAD

=======
class CrearCita(CreateView):
	model = Cita
	fields =[
		'nomPac',
		'apePac',
		'telPac',
		'fecCon',
	]

# Create your views here.
>>>>>>> b044f7f65bcc261f7ee9bfe1c3fcb2387f211f4a

def index(request):   

    return render(
        request,
        'base/base.html',
        context={},
    )

# Vista de la creacion de cita
class CrearCita(CreateView):
	model = Cita
	template_name = 'citasyconsultas/cita_form.html'
	form_class = NuevaCitaForm
	success_url = reverse_lazy('/')

# Listar los servicios disponibles
class ListarServicio(ListView):
	model = Servicio
	template_name = 'citasyconsultas/servicio_list.html'
	form_class = ServicioForm
	success_url = reverse_lazy('/')


#modelos de Medicamento
class ListadoMedicamento(ListView):
    model = Medicamento
    template_name = 'citasyconsultas/GestionMedicamento.html'
    context_object_name = 'medicamentos'

class crearMedicamento(CreateView):
    template_name = 'citasyconsultas/crearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class modificarMedicamento(UpdateView):
    model = Medicamento
    template_name = 'citasyconsultas/crearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class eliminarMedicamento(DeleteView):
    model = Medicamento
    template_name='citasyconsultas/eliminarMedicamento.html'
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

