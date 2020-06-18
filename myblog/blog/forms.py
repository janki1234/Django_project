from django import forms
from .models import Blog
class DateInput(forms.DateInput):
		input_type='date'

		
class BlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields='__all__'
		widgets={
			'date':DateInput()
		}