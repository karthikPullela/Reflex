from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import requests

# Create your views here.
def home(request):
	r = requests.get('https://www.google.com')
	return render(request, 'home/home.html', {'r':r})