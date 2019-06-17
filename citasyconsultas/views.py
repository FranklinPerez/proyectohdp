from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

def index(request):   

    return render(
        request,
        'base/base.html',
        context={},
    )
#modelos de Medicamento
class ListadoMedicamento(ListView):
    model = Medicamento
    template_name = 'citasyconsultas/gestionMedicamento.html'
    context_object_name = 'medicamentos'

class crearMedicamento(CreateView):
    template_name = 'citasyconsultascrearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class modificarMedicamento(UpdateView):
    model = Medicamento
    template_name = 'citasyconsultas/crearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class eliminarMedicamento(DeleteView ):
    model = Medicamento
    template_name='citasyconsultas/eliminarMedicamento.html'
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')