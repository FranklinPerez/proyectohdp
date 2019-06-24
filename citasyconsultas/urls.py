
from django.urls import path, include
from .views import *

app_name = 'citasyconsultas'
urlpatterns=[
	path('index/', index, name='index'),
	#views para medicamento
	path('gestionMedicamento/', ListadoMedicamento.as_view(), name='listado_medicamento'),
	path('crearMedicamento/', crearMedicamento.as_view(), name='crear_medicamento'),
	path('modificarMedicamento/<int:pk>/', modificarMedicamento.as_view(), name='modificar_medicamento'),
	path('eliminarMedicamento/<int:pk>/', eliminarMedicamento.as_view(), name='eliminar_medicamento'),

	# URL's y VIEWS para el control de las citas
	path('nueva_cita/', CrearCita.as_view(), name = 'nueva_cita'),
	path('gestion_cita/', GestionCitas.as_view(), name = 'gestion_cita'),
	path('modificar_cita/<int:pk>/', ModificarCita.as_view(), name = 'modificar_cita'),
	path('cancelar_cita/<int:pk>/', CancelarCita.as_view(), name = 'cancelar_cita'),
	path('cobrar/', RealizarCobro, name = 'cobrar'),
	path('citasParaHoy/', citasParaHoy, name='gestion_cita'),path('verCita/<int:pk>/', verCita.as_view(), name='verCita'),
	path('verCita/<int:pk>/', verCita.as_view(), name='verCita'),



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
	path('crearConsulta', crearConsulta.as_view(), name='crear_consulta'),

	path('iniciarSesion', iniciarSesion, name='inicar_sesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),
]

