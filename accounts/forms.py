# forms.py
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import FileInput, TextInput, EmailInput

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    # username = UsernameField(help_text=None)
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    first_name = forms.CharField(max_length=30, help_text=None, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(help_text=None, widget=EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, help_text=None, widget=TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text=None, label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), strip=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(widget=FileInput, required=False)
    phone_number = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['picture', 'phone_number']  # Add more fields as needed


class LoginForm(forms.Form):
    email = forms.EmailField(help_text=None, label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(help_text=None, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), strip=False)
    captcha = ReCaptchaField(widget=ReCaptchaV3)

# class EditProfile(forms.Form):
#     picture = forms.ImageField(widget=FileInput, required=False)
#     phone_number = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=30, help_text=None, widget=TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(help_text=None, widget=EmailInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=30, help_text=None, widget=TextInput(attrs={'class': 'form-control'}))
