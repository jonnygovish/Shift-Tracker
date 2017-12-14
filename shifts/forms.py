from django import forms
from .models import Employee_profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

class EmployeeProfileForm(forms.ModelForm):
  class Meta:
    model = Employee_profile
    fields = ('phonenumber', 'date_of_birth','profile_pic',)
