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
# Types of users
STUDENT = 1
ADMIN = -1
INVIGILATOR = 2
USER_CHOICE = (
	(STUDENT,'Student'),
	(INVIGILATOR, 'Invigilator'),
	(ADMIN, 'Admin'),
)