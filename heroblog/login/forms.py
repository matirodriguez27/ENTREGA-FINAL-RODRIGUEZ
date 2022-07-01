from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.views.generic import CreateView

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= "modificar email",widget=forms.EmailInput)
    password1= forms.CharField(label='modificar contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_texts = {k:"" for k in fields}