from django.db import models

# Create your models here.
class Students(models.Model):
	# Different Years of study.
	FIRST = 1
	SECOND = 2
	THIRD = 3
	FOURTH = 4
	YEAR_CHOICES = (
		(FIRST,'1st Year'),
		(SECOND,'2nd Year'),
		(THIRD,'3rd Year'),
		(FOURTH, '4rth Year'),
	)
	# Different classes of study of a student.
	BTECH = 'B.Tech'
	MTECH = 'M.Tech'
	PHD = 'P.hD'
	CLASS_CHOICES = (
		(BTECH,'B.Tech'),
		(MTECH,'M.Tech'),
		(PHD,'PHD'),
	)
	# Sections of study of a student.
	SECA = 'A'
	SECB = 'B'
	SECC = 'C'
	SECD = 'D'
	SECE = 'E'
	SECF = 'F'
	SECG = 'G'
	SECH = 'H'
	SECI = 'I'
	SECJ = 'J'
	SECK = 'K'
	SECL = 'L'
	SECM = 'M'
	SECN = 'N'
	SECNO = 'NO'
	SECTION_CHOICES = (
		(SECA,'Section A'),
		(SECB,'Section B'),
		(SECC,'Section C'),
		(SECD,'Section D'),
		(SECE,'Section E'),
		(SECF,'Section F'),
		(SECG,'Section G'),
		(SECH,'Section H'),
		(SECI,'Section I'),
		(SECJ,'Section J'),
		(SECK,'Section K'),
		(SECL,'Section L'),
		(SECM,'Section M'),
		(SECN,'Section N'),
		(SECNO, 'No Section Allotted'),
	)
	# Branches of study.
	BIOTECH = 'Bio Technology'
	CSE = 'Computer Science and Engineering'
	CE = 'Civil Engineering'
	MECH = 'Mechanical Engineering'
	EEE = 'Electrical and Electronics Engineering'
	CIVIL = 'Civil Engineering'
	ECE = 'Electronics and Communication Engineering'
	MME = 'Metallurgical and Materials Engineering'
	CHE = 'Chemical Engineering'
	MATH = 'Mathematics'
	PHYS = 'Physics'
	CHEM = 'Chemistry'
	HASS = 'Humanities and Social Sciences'
	SOM  = 'School of Management'
	BRANCH_CHOICES = (
		(BIOTECH,'Bio Technology'),
		(CSE, 'Computer Science & Engineering'),
		(CE, 'Civil Engineering'),
		(MECH, 'Mechanical Engineering'),
		(EEE, 'Electical and Electronics Engineering'),
		(CIVIL, 'Civil Engineering'),
		(ECE, 'Electronics and Communication Engineering'),
		(MME, 'Metallurgical and Materials Engineering'),
		(CHE, 'Chemical Engineering'),
		(MATH, 'Mathematics'),
		(PHYS, 'Physics'),
		(CHEM, 'Chemistry'),
		(HASS, 'Humanities and Social Sciences'),
		(SOM, 'School of Management'),
	)
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
	# Branches of study.
	BIOTECH = 'Bio Technology'
	CSE = 'Computer Science and Engineering'
	CE = 'Civil Engineering'
	MECH = 'Mechanical Engineering'
	EEE = 'Electrical and Electronics Engineering'
	CIVIL = 'Civil Engineering'
	ECE = 'Electronics and Communication Engineering'
	MME = 'Metallurgical and Materials Engineering'
	CHE = 'Chemical Engineering'
	MATH = 'Mathematics'
	PHYS = 'Physics'
	CHEM = 'Chemistry'
	HASS = 'Humanities and Social Sciences'
	SOM  = 'School of Management'
	BRANCH_CHOICES = (
		(BIOTECH,'Bio Technology'),
		(CSE, 'Computer Science & Engineering'),
		(CE, 'Civil Engineering'),
		(MECH, 'Mechanical Engineering'),
		(EEE, 'Electical and Electronics Engineering'),
		(CIVIL, 'Civil Engineering'),
		(ECE, 'Electronics and Communication Engineering'),
		(MME, 'Metallurgical and Materials Engineering'),
		(CHE, 'Chemical Engineering'),
		(MATH, 'Mathematics'),
		(PHYS, 'Physics'),
		(CHEM, 'Chemistry'),
		(HASS, 'Humanities and Social Sciences'),
		(SOM, 'School of Management'),
	)
	# Other information that is needed for the Invigilators
	empid = models.CharField(unique=True, max_length=100)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	branch = models.CharField(choices=BRANCH_CHOICES, default=BIOTECH, max_length=100)
	# Username should also be present here.

class Auth(models.Model):
	# Types of users
	STUDENT = 1
	ADMIN = -1
	INVIGILATOR = 2
	USER_CHOICE = (
		(STUDENT,'Student'),
		(INVIGILATOR, 'Invigilator'),
		(ADMIN, 'Admin'),
	)
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
