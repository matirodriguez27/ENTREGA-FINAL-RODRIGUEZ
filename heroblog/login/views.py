from ast import AugStore
from io import UnsupportedOperation
from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contra)
            if user is not None:
                login(request,user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"inicio.html", {"mensaje":"Error"})
        else:
            return render(request,"inicio.html", {"mensaje":"Error"})
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

