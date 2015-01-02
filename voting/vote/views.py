from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from vote.models import Students, Invigilators, Contestants, Campaigning

def index(request):
	try:
		user = request.user
		print user
		if user.is_authenticated and user != AnonymousUser:
			return render(request,'loggedin.html',{'username':user})
	except:	
		return render(request, 'index.html')

def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				context_dict = {'username':username}
				return render(request,'loggedin.html',context_dict)
			else:
				context_dict = {'username':username, 'checking':1, 'message':"User Disabled. Please contact administrator"}
				return render(request,'login.html')
		else:
			context_dict = {'username':username, 'checking':1, 'message':"Your username or password is incorrect."}
			return render(request,'login.html', context_dict)
	context_dict = {'checking':0, 'message':"Please login"}
	return render(request, 'login.html')

def signuppage(request):
	if request.method == 'POST':
		users = User()
		users.username = request.POST['username']
		users.password = request.POST['password']
		users.email = request.POST['email']
		user = User.objects.create_user(users.username, users.password, users.email)
		print user.id
		student = Students()
		student.userdetail = user
		student.regno = request.POST['regno']
		student.rollno = request.POST['rollno']
		student.year = request.POST['year']
		student.branch = request.POST['branch']
		student.studyclass = request.POST['studyclass']
		student.section = request.POST['section']
		student.voted = 0
		student.save()
		context_dict = {'message':'You have successfully registered.', 'checking':1}
		return render(request, 'login.html', context_dict)
	return render(request, 'signup.html')

def logoutpage(request):
	print "Logout Request Sent!"
	logout(request)
	return HttpResponseRedirect("/")
