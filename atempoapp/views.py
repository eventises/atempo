from django.views.generic import View
from django.template.response import TemplateResponse
from atempoapp.models import Atempo
from django.http import HttpResponseRedirect

class AtempoViewAll(View):
	def get(self, request, *args, **kwargs):
		context = {
            'msg_list': Atempo.objects.all().order_by('-id')
        }
		return TemplateResponse(request, 'msglist.html', context)
class AtempoNewMsg(View):
	def get(self, request, *args, **kwargs):
		return TemplateResponse(request, 'newmsg.html', {})

class AtempoSave(View):
	def post(self, request, *args, **kwargs):
		name = request.POST['name']
		message = request.POST['message']
		email = request.POST['email']
		Atempo.objects.create(name=name,message=message,email=email)
		return HttpResponseRedirect('/')
