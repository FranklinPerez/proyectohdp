from django.db.models import Q


from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from datetime import *
from .models import *
from .forms import *
from django.views.generic.detail import DetailView
from django.views import View

from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def index(request):   

    return render(
        request,
        'base/base.html',
        context={},
    )
# CITA Y SU CRUD==============================================================
class CrearCita(CreateView):
    template_name = 'citasyconsultas/cita_form.html'
    form_class = NuevaCitaForm
    success_url = reverse_lazy('citasyconsultas:gestion_cita')


class GestionCitas(ListView):
	model = Cita
	template_name = 'citasyconsultas/gestionCitas.html'
	context_object_name = 'citas'


class ModificarCita(UpdateView):
    template_name = 'citasyconsultas/modificarCita.html'
    model = Cita
    form_class = ModificarCitaForm
    success_url = reverse_lazy('citasyconsultas:gestion_cita')
    

class CancelarCita(DeleteView):
    template_name = 'citasyconsultas/cancelarCita.html'
    model = Cita
    success_url = reverse_lazy('citasyconsultas:gestion_cita')

def citasParaHoy(request):
    fechahoy=datetime.now().date()
    citas=Cita.objects.filter(fecCitHoy__contains=fechahoy)            
    return render(request, 'citasyconsultas/citasParaHoy.html',context={'citas':citas})

class verCita(DetailView):
    template_name = 'citasyconsultas/verCita.html'
    model = Cita
   ## context_object_name = 'verCita'
    ##success_url = reverse_lazy('citasyconsultas:gestion_cita')


#==========================================================================
#REALIZAR COBRO============================================================
def RealizarCobro(request):
    query = request.GET.get('q')
    hoy = datetime.now().date()
    qset = (Q(numCit = query) & Q(fecCon__contains = hoy))
    results = Cita.objects.filter(qset)

    return render(request, 'citasyconsultas/cobro.html',context={'cita_a_cobrar':results})
          
#==========================================================================


#modelos de Medicamento
class ListadoMedicamento(ListView):
    model = Medicamento
    template_name = 'citasyconsultas/gestionMedicamento.html'
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

#modelos de Servicio
class ListadoServicio(ListView):
    model = Servicio
    template_name = 'citasyconsultas/gestionServicio.html'
    context_object_name = 'servicios'

class crearServicio(CreateView):
    template_name = 'citasyconsultas/crearServicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('citasyconsultas:listado_servicio')

class modificarServicio(UpdateView):
    model = Servicio
    template_name = 'citasyconsultas/crearServicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('citasyconsultas:listado_servicio')

class eliminarServicio(DeleteView):
    model = Servicio
    template_name='citasyconsultas/eliminarServicio.html'
    success_url = reverse_lazy('citasyconsultas:listado_servicio')




class BuscarExpediente(ListView):
    model = Paciente
    template_name = 'citasyconsultas/gestionExpediente.html'
    context_object_name = 'expedientes'

class crearExpediente(CreateView):
    template_name = 'citasyconsultas/crearExpediente.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('citasyconsultas:listado_expediente')

class modificarExpediente(UpdateView):
    model = Paciente
    template_name = 'citasyconsultas/crearExpediente.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('citasyconsultas:listado_expediente')



def consultasPendientes(request):
    fechahoy=datetime.now().date()
    consultas=Consulta.objects.filter(estado='p').filter(fecConHoy__contains=fechahoy)            
    return render(request, 'citasyconsultas/consultasPendientes.html',context={'consultas':consultas})

class modificarConsulta(UpdateView):
    model = Consulta
    template_name = 'citasyconsultas/modificarConsulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('citasyconsultas:listado_consulta')

class crearConsulta(CreateView):   
    template_name = "citasyconsultas/crearConsulta.html"
    form_class = nuevaConsultaForm
    success_url = reverse_lazy('citasyconsultas:gestion_cita')


   
def iniciarSesion(request):   

    return render(
        request,
        'citasyconsultas/login.html'
    )

def autenticarUsuario(request):
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        filtro = Usuario.objects.filter(codUsu=username).filter(pasUsu=password).values('tipo_usuario')
        if filtro:
            if filtro[0].get('tipo_usuario')=='m':           
                return redirect('citasyconsultas:listado_consulta')            
            else:
                if filtro[0].get('tipo_usuario')=='s': 
                    return redirect('citasyconsultas:gestion_cita')
        else:   
            return render(request,'citasyconsultas/errorUsuario.html')
                
                
        
def cerrarSesion(request):
    return render(request,'citasyconsultas/login.html')


def ir_a_medicamento(request):
    return redirect('citasyconsultas:listado_medicamento')

def ir_a_servicio(request):
    return redirect('citasyconsultas:listado_servicio')





        