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
		if user.is_authenticated and user != AnonymousUser:
			return HttpResponseRedirect('/dashboard')
	except:	
		return render(request, 'index.html')

def dashboard(request):
	return render(request,'dashboard.html')

def is_member(user,member):
    return user.groups.filter(name=member).exists()

def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active and is_member(user,"Student"):
				login(request,user)
			elif user.is_active and is_member(user,"Moderator"):
				print is_member(user,"Moderator")
				login(request,user)
				messages.info(request,"Hey Moderator! ")
			else:
				messages.info(request,"User Disabled. Please contact administrator")
				return HttpResponseRedirect('/login')
			return HttpResponseRedirect('/dashboard')
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
		user = User.objects.create_user(users.username,users.email, users.password)
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
		return HttpResponseRedirect('/login')
	myform=StudentForm()
	return render(request, 'signup.html',{'myform':myform})

def logoutpage(request):
	print "Logout Request Sent!"
	logout(request)
	return HttpResponseRedirect("/")
