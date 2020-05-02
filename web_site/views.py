from django.urls import reverse
from django.shortcuts import render
# Create your views here.

def home(request):
	return render(request, 'base.html')

def how_to(request):
	return render(request, 'web_site/how_to.html')
