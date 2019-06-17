<<<<<<< HEAD
from django.urls import path, include
from .views import *

<<<<<<< HEAD

urlpatterns = [
	path('nueva_cita/', views.CrearCita.as_view(), name = 'nueva_cita'),
]
=======
from django.urls import path, include


app_name = 'citasyconsultas'
>>>>>>> b4ca0ebcdf8fbe2b519dce899922db8e11b985c3
=======
app_name = 'citasyconsultas'
urlpatterns=[
	path('gestionMedicamento/', ListadoMedicamento.as_view(), name="listado_medicamento"),
	path('crearMedicamento/', crearMedicamento.as_view(), name="crear_medicamento"),
	path('modificarMedicamento/<int:pk>/',modificarMedicamento.as_view(), name="modificar_medicamento"),
	path('eliminarMedicamento/<int:pk>/', eliminarMedicamento.as_view(), name="eliminar_medicamento"),
]
>>>>>>> e61d06ba1b655322d1ce9f18c9daa07f775672c8
