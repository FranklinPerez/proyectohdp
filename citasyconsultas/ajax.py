from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import render
from .models import *


def load_Municipio(request):
	depId = request.GET.get('depId')
	municipios = Municipio.objects.filter(departamento_id = depId)
	
	return render(request, 'hr/mun_dropdown_list.html', context={'mun': municipios})


def load_Horario(request):
	date = request.GET.get('fecha')
	horarios = Horario.objects.exclude(cita__fecCon = date)

	return render(request, 'hr/hora_dropdown_list.html', context={'horas': horarios})

