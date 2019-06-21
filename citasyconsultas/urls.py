
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
	path('lista_servicio/', ListarServicio.as_view(), name = 'lista_servicio'),
	path('gestion_servicio/', GestionServicio.as_view(), name = 'gestion_servicio'),
	path('agregar_servicio/', AgregarServicio.as_view(), name = 'agregar_servicio'),
	path('modificar_servicio/', ModificarServicio.as_view(), name = 'modificar_servicio'),
	path('eliminar_servicio/', EliminarServicio.as_view(), name = 'eliminar_servicio'),
]

