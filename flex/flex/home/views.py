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
	raw_data = open(file_path, 'rt')
	my_data = json.load(raw_data)
	raw_data.close()
	walk_data = []
	i = 0
	while i < len(my_data['bucket']):
		walk_data.append(my_data['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
		i = i+1

	file_path = os.path.join(module_dir, 'static/home/calories.json')
	raw_data = open(file_path, 'rt')
	my_data = json.load(raw_data)
	raw_data.close()
	calories_data = []
	i = 0
	while i < len(my_data['bucket']):
		calories_data.append(my_data['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
		i = i+1

	return render(request, 'home/home.html', 
		{
		'calories_data':calories_data,
		'walk_data':walk_data,
		})

def log(request):
	return render(request, 'home/login.html')



def user_login(request):
	username = 'devam'
	password = 'devamdevam'
	auth_user = authenticate(request, username=username, password=password)
	if auth_user is not None:
		login(request, auth_user)
		#return HttpResponse(request.user.username)
		return redirect('dash') # -----------
	else:
		return HttpResponse("Unable to log in. User not found. <br>Please check superuser for more details.")
	return HttpResponse("It's not supposed to come till here.")


def return_data(request):
	if request.user.is_authenticated:
		uri = 'https://www.googleapis.com/fitness/v1/users/me/dataSources'
		r = requests.get(uri)
		return HttpResponse("Works, I guess.", auth=(request.user.username, request.user.password))
	else:
		return HttpResponse("User not authenticated")



def dash(request):

	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'static/home/fit.json')
	raw_data = open(file_path, 'rt')
	my_data = json.load(raw_data)
	raw_data.close()
	walk_data = []
	i = 0
	while i < len(my_data['bucket']):
		walk_data.append(my_data['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
		i = i+1

	file_path = os.path.join(module_dir, 'static/home/calories.json')
	raw_data = open(file_path, 'rt')
	my_data = json.load(raw_data)
	raw_data.close()
	calories_data = []
	i = 0
	while i < len(my_data['bucket']):
		calories_data.append(my_data['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
		i = i+1

	return render(request, 'home/dashboard.html', 
		{
		'calories_data':calories_data,
		'walk_data':walk_data,
		})