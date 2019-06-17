from django.urls import path, include
from .views import *

app_name = 'citasyconsultas'
urlpatterns=[
	path('gestionMedicamento/', ListadoMedicamento.as_view(), name="listado_medicamento"),
	path('crearMedicamento/', crearMedicamento.as_view(), name="crear_medicamento"),
	path('modificarMedicamento/<int:pk>/',modificarMedicamento.as_view(), name="modificar_medicamento"),
	path('eliminarMedicamento/<int:pk>/', eliminarMedicamento.as_view(), name="eliminar_medicamento"),
]