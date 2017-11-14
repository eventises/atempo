from django.views.generic import View
from django.template.response import TemplateResponse
from atempoapp.models import Atempo

class AtempoViewAll(View):
	def get(self, request, *args, **kwargs):
		context = {
            'msg_list': Atempo.objects.all()
        }
		return TemplateResponse(request, 'msglist.html', context)
