from django.urls import reverse
from django.shortcuts import render
import os
# Create your views here.

def hello(request):
	return render(request, 'base.html')
