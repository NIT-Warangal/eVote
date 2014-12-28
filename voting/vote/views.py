from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.http import HttpResponse
from vote.models import Students, Invigilators, Contestants, Campaigning

def index(request):
	context_dict = {'message': "Welcome to the eVoting System to select the student council"}
	return render(request, 'index.html', context_dict)

def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'loggedin.html')
			else:
				context_dict = {'username':username, 'checking':1, 'message':"User Disabled. Please contact administrator"}
				return render(request,'login.html')
		else:
			context_dict = {'username':username, 'checking':1, 'message':"No user like this exists"}
			return render(request,'login.html', context_dict)
	context_dict = {'checking':0, 'message':"Please login"}
	return render(request, 'login.html')