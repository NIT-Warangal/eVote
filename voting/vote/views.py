from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from vote.models import Students, Invigilators, Contestants, Campaigning
from vote.forms import StudentForm

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
				messages.info(request,"User Disabled. Please contact administrator")
				return render(request,'login.html')
		else:
			messages.error(request,"Your username or password is incorrect.")
			return HttpResponseRedirect('/login')
	messages.success(request, "Please login")
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
		messages.success(request,"You have registered successfully.")
		return render(request, 'login.html')
	myform=StudentForm()
	return render(request, 'signup.html',{'myform':myform})

def logoutpage(request):
	print "Logout Request Sent!"
	logout(request)
	return HttpResponseRedirect("/")
