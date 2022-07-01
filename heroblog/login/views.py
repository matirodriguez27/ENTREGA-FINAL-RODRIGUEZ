from login.forms import UserRegisterForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contrasena)
            if user is not None:
                login(request, user)
                return render(request, "login.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"index.html", {"mensaje":"Error"})
        else:
            return render(request,"index.html", {"mensaje":"Error"})
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            return render(request, "index.html")
    else:
        form = UserRegisterForm()
        return render(request, "signup.html", {'form':form})