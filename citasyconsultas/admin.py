from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Servicio)
admin.site.register(Cita)
admin.site.register(Medico)
admin.site.register(Usuario)
admin.site.register(Consulta)

admin.site.register(Paciente)

admin.site.register(Departamento)
admin.site.register(Municipio)



