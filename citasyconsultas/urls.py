<<<<<<< HEAD
from django.urls import url, path, include
from .views import *


urlpatterns = [
	url(r'nueva_cita/', views.CrearCita.as_view(), name = 'nueva_cita'),
]
=======
from django.urls import path, include


app_name = 'citasyconsultas'
>>>>>>> b4ca0ebcdf8fbe2b519dce899922db8e11b985c3
