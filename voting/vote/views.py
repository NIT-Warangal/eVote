from django.shortcuts import render

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
		context_dict = {'username':username, 'password':password}
		return render(request,'loggedin.html', context_dict)
	return render(request, 'login.html')