from django import forms
from vote.models import Students, Invigilators, Contentants, Campaigning
from constants import YEAR_CHOICES, CLASS_CHOICES, SECTION_CHOICES, BRANCH_CHOICES, USER_CHOICE, FIRST, BIOTECH, BTECH, SECA

# Forms related content being generated here.
class StudentForm(forms.ModelForm):
	regno = forms.CharField(label='Registration No', max_length=100)
	rollno = forms.CharField(label='Roll No.', max_length=100)
	year = forms.ChoiceField(label='Year of Study', choices=YEAR_CHOICES)
	exclude(voted, userdetail, )
	class Meta:
		Students
