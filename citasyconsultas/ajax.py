from django.http import JsonResponse
from django.shortcuts import render
from .models import Municipio


def load_Municipio(request):
	depId = request.GET.get('depId')
	municipios = Municipio.objects.filter(departamento_id = depId)
	
	return render(request, 'hr/mun_dropdown_list.html', context={'mun': municipios})


def load_Mun(request):
	depId = request.GET.get('depId')
	municipios = Municipio.objects.none()
	options = '<option value="" selected = "selected">-----------</option>'
	if depId:
		municipios = Municipio.objects.filter(departamento_id = depId)
	for m in municipios:
		options += '<option value ="%s">%s</option>' % (m.pk, m.nomMunicipio)
	response = {}
	response['municipios'] = options
	return JsonResponse(response)