from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

attrs = {"class": "form-control"}

class UserLoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update(
			{'placeholder': 'Enter your username'})
		self.fields['password'].widget.attrs.update(
			{'placeholder': 'Enter your password'})

	username = forms.CharField(
		label="Username",
		widget=forms.TextInput(attrs=attrs))

	password = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(attrs=attrs))


class UserRegisterForm(UserCreationForm):

	first_name = forms.CharField(
		label="First Name",
		widget=forms.TextInput(
			attrs={"class": "form-control",
			       'placeholder': 'Enter your first name'}))
	last_name = forms.CharField(
		label="Last Name",
		widget=forms.TextInput(
			attrs={"class": "form-control",
			       'placeholder': 'Enter your last name'}))
	username = forms.CharField(
		label="Username",
		widget=forms.TextInput(
			attrs={"class": "form-control",
			       'placeholder': 'Enter your username '}))
	email = forms.EmailField(
		label="Email",
		widget=forms.TextInput(
			attrs={"class": "form-control",
			       'placeholder': 'Enter your email'}))

	password1 = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(
			attrs={"class": "form-control",
			       'placeholder': 'Enter your password'}))
	password2 = forms.CharField(
		label="Confirm Password",
		strip=False,
		widget=forms.PasswordInput(
			attrs={"class": "form-control",
			       'placeholder': 'Confirm your password'}))

	class Meta(UserCreationForm.Meta):
		fields = ("first_name", "last_name", "username", "email")


class ProfileForm(UserChangeForm):
	password = None

	class Meta:
		model = User
		fields = ["first_name", "last_name", "email"]
		widgets = {
			"first_name": forms.TextInput(attrs=attrs),
			"last_name": forms.TextInput(attrs=attrs),
			"email": forms.EmailInput(attrs=attrs)
		}