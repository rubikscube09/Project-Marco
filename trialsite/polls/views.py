from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("It's working...sort of")

# Create your views here.
