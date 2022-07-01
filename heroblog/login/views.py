from login.forms import UserRegisterForm, UserEditForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
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
                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request,"index.html", {"mensaje":"Formulario invalido"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form':form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, "index.html", {"mensaje":"Usuario registrado"})
        else:
            return render(request,"index.html", {"mensaje":"Formulario invalido"})
    else:
        form = UserCreationForm()
        return render(request, "signup.html", {"form":form})

def userEdit(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "index.html")
        else:
            return render(request,"index.html", {"mensaje":"Formulario invalido"})
    else:
        form = UserEditForm(initial={'email':usuario.email})
        return render(request, "useredit.html", {"form":form, "usuario": usuario})