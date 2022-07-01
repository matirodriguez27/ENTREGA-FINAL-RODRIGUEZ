from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password','password2',]
        help_texts = {k:"" for k in fields}