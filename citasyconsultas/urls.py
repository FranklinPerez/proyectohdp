
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
	#views para cita
	path('nueva_cita/', CrearCita.as_view(), name = 'nueva_cita'),
	path('lista_servicios/', ListarServicio.as_view(), name = 'lista_servicios'),
	#views para servicio
	path('gestionServicio/', ListadoServicio.as_view(), name='listado_servicio'),
	path('crearServicio/', crearServicio.as_view(), name='crear_servicio'),
	path('modificarServicio/<int:pk>/', modificarServicio.as_view(), name='modificar_servicio'),
	path('eliminarServicio/<int:pk>/', eliminarServicio.as_view(), name='eliminar_servicio'),
]

