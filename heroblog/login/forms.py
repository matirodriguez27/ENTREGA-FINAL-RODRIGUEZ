from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.views.generic import CreateView

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label= "modificar apodo", widget= forms.TextInput)
    password1= forms.CharField(label='modificar contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','password1','password2']
        help_texts = {k:"" for k in fields}