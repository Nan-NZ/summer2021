from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	index_template = loader.get_template('jordan/index.html')
	context = {}
	return HttpResponse(index_template.render(context, request))