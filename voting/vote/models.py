from django.db import models
from django.contrib.auth.models import User
from constants import YEAR_CHOICES, CLASS_CHOICES, SECTION_CHOICES, BRANCH_CHOICES, USER_CHOICE, FIRST, BIOTECH, BTECH, SECA

# Create your models here.
class Students(models.Model):
	# Other details that are needed.
	userdetail = models.ForeignKey(User, null=True)
	regno = models.CharField(unique=True, max_length=100)
	rollno = models.CharField(unique=True, max_length=100)
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
	userdetail = models.ForeignKey(User, null=True)

class Contestants(models.Model):
	contestantId = models.AutoField(primary_key=True)
	regno = models.CharField(unique=True, max_length=100)
	contestant_photo = models.ImageField(upload_to='contestants/', null=False, blank=False)
	nomineeregno = models.CharField(unique=True, max_length=100)
	nominee_photo = models.ImageField(upload_to='nominees/', null=False, blank=False)
	short_code = models.CharField(unique=True, max_length=10)
	votecount = models.IntegerField(default=0)

class Campaigning(models.Model):
	contestantId = models.CharField(max_length=100)
	Content = models.CharField(max_length=10000)
	# Content should be taken in |safe mode from a WYSISYG editor
