from django.db import models
from constants import YEAR_CHOICES, CLASS_CHOICES, SECTION_CHOICES, BRANCH_CHOICES, USER_CHOICE, FIRST, BIOTECH, BTECH, SECA

# Create your models here.
class Students(models.Model):
	# Other details that are needed.
	regno = models.CharField(unique=True, max_length=100)
	rollno = models.CharField(unique=True, max_length=100)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	year = models.IntegerField(choices=YEAR_CHOICES, default=FIRST)
	branch = models.CharField(choices=BRANCH_CHOICES, default=BIOTECH, max_length=100)
	studyclass = models.CharField(choices=CLASS_CHOICES, default=BTECH, max_length=100)
	section = models.CharField(choices=SECTION_CHOICES, default=SECA, max_length=10)
	voted = models.BooleanField(default=False)
	# Username should be here to map these fields with the authentication.

class Invigilators(models.Model):
	# Other information that is needed for the Invigilators
	empid = models.CharField(unique=True, max_length=100)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	branch = models.CharField(choices=BRANCH_CHOICES, default=BIOTECH, max_length=100)
	# Username should also be present here.

class Auth(models.Model):
	# Details
	Username = models.CharField(unique=True, max_length=18)
	email = models.EmailField(unique=True)
	Password = models.CharField(max_length=500) # Need to hash
	user_type = models.IntegerField()

class Contestants(models.Model):
	contestantId = models.AutoField(primary_key=True)
	regno = models.CharField(unique=True, max_length=100)
	contestant_photo = models.ImageField(upload_to='contestants/', null=False, blank=False)
	nomineeregno = models.CharField(unique=True, max_length=100)
	nominee_photo = models.ImageField(upload_to='nominees/', null=False, blank=False)
	short_code = models.CharField(unique=True, max_length=10)

class Campaigning(models.Model):
	contestantId = models.CharField(max_length=100)
	Content = models.CharField(max_length=10000)
	# Content should be taken in |safe mode from a WYSISYG editor
