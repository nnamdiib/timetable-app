from django import forms

class CourseCodeForm(forms.Form):
	code = forms.CharField(label='', max_length=6)

