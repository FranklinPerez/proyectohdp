from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'nueva_cita/', views.CrearCita.as_view(), name = 'nueva_cita'),
]