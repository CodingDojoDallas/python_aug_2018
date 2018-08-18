from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

import bcrypt

def home(request):
	return render(request, 'login_app/forms.html')

def process(request):
	errors = User.objects.validation_registration(request.POST)
	if len(errors) == 0:
		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(name=request.POST['name'], email=request.POST['email'], password=hashpw)
		request.session['id'] = user.id
		return redirect('/success')
		#return render(request, 'login_app/success.html')
	for e in errors:
		messages.error(request, e)
	return redirect('/')

def success(request):
	context ={
		'user': User.objects.get(id = request.session['id'])
	}
	return render(request, 'login_app/success.html', context)

def login(request):
	errors = User.objects.validation_login(request.POST)
	if len(errors) != 0:
		for e in errors:
			messages.error(request, e)
		return redirect('/')
	user = User.objects.filter(email=request.POST['email'])
	request.session['id'] = user[0].id
	return redirect('/success')