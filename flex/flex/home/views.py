from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate

import requests
import os
import json

# Create your views here.
def home(request):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'static/home/fit.json')
	#json_file_name = '../../static/home/fit.json'
	raw_data = open(file_path, 'rt')
	my_data = json.load(raw_data)
	raw_data.close()
	walk_data = []
	i = 0
	while i < len(my_data['bucket']):
		walk_data.append(my_data['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
		i = i+1
	#my_data['bucket'][0]['dataset'][0]['point'][0]['value'][0]['intVal']
	return render(request, 'home/home.html', {'r':walk_data})

def user_login(request):
	username = 'devam'
	password = 'devamdevam'
	auth_user = authenticate(request, username=username, password=password)
	if auth_user is not None:
		login(request, auth_user)
		return redirect('home') # -----------
	else:
		return HttpResponse("Unable to log in. User not found. <br>Please check superuser for more details.")
	return HttpResponse("It's not supposed to come till here.")