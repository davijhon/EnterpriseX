from django.contrib.auth import get_user_model
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = get_user_model()
		fields = ('email', 'username',)
		widgets = {
          'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}),
		  'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
		

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = get_user_model()
		fields = ('email', 'username',)