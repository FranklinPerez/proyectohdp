
from django.urls import path
from .views import *


app_name = 'citasyconsultas'
urlpatterns=[
	path('index/', index, name='index'),
	#views para medicamento
	path('gestionMedicamento/', ListadoMedicamento.as_view(), name='listado_medicamento'),
	path('crearMedicamento/', crearMedicamento.as_view(), name='crear_medicamento'),
	path('modificarMedicamento/<int:pk>/', modificarMedicamento.as_view(), name='modificar_medicamento'),
	path('eliminarMedicamento/<int:pk>/', eliminarMedicamento.as_view(), name='eliminar_medicamento'),


	path('nueva_cita/', CrearCita.as_view(), name = 'nueva_cita'),
	path('gestion_cita/', GestionCitas.as_view(), name = 'gestion_servicio'),
	path('modificar_cita/<int:pk>/', ModificarCita.as_view(), name = 'modificar_cita'),
	path('eliminar_cita/<int:pk>/', EliminarCita.as_view(), name = 'eliminar_cita'),


	#views para servicio
	path('gestionServicio/', ListadoServicio.as_view(), name='listado_servicio'),
	path('crearServicio/', crearServicio.as_view(), name='crear_servicio'),
	path('modificarServicio/<int:pk>/', modificarServicio.as_view(), name='modificar_servicio'),
	path('eliminarServicio/<int:pk>/', eliminarServicio.as_view(), name='eliminar_servicio'),

	#views para exp
	path('gestionExpediente/', BuscarExpediente.as_view(), name='listado_expediente'),
	path('crearExpediente/', crearExpediente.as_view(), name='crear_expediente'),
	path('modificarExpediente/<int:pk>/', modificarExpediente.as_view(), name='modificar_expediente'),


	#views para consulta
	path('consultasPendientes/', consultasPendientes, name='listado_consulta'),
	path('modificarConsulta/<int:pk>/', modificarConsulta.as_view(), name='modificar_consulta'),



]

