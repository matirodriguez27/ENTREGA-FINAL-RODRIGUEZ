from login.forms import UserRegisterForm, UserEditForm, UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contrasena)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request,"error.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request,"error.html", {"mensaje":"Formulario invalido"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form':form})

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"error.html", {"mensaje":"Formulario invalido"})
    else:
        form = UserRegisterForm()
        return render(request, "signup.html", {"form":form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='inicio')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
