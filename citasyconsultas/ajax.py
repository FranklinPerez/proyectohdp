from django.http import JsonResponse
from .models import Municipio



def load_Municipio(request):
	depId = request.GET.get('depResidencia')
	municipios = Municipio.objects.none()
	options = '<option value="" selected = "selected">-----------</option>'
	if depId:
		municipios = Municipio.objects.filter(departamento_id = depId)
	for m in municipios:
		options += '<option value ="%s">%s</option>' % (m.pk, m.nomMuicipio)
	response = {}
	response['municipios'] = options
	return JsonResponse(response)