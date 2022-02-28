from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from theblog.models import Profile, CustomUser
from django.conf import settings

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'website_url', 'fb_url', 'insta_url')
		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			# 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
			'website_url': forms.TextInput(attrs={'class': 'form-control'}),
			'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
			'insta_url': forms.TextInput(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
		}


class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = ('username', 'first_name', 'last_name', 'email',  'last_login', 'is_superuser', 'is_staff','is_active', 'date_joined')


class PasswordChangingform(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = ('old_password', 'new_password1', 'new_password2')
