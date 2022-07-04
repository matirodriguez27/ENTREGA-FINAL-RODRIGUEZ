from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse_lazy 
from .forms import PostForm
from django.utils import timezone

class ListaPosts(ListView):
    model = Post
    template_name="listaposts.html"
class DetallePost(DetailView):
    model = Post
    template_name="detallepost.html"
class EditarPost(UpdateView):
    model = Post
    template_name = ""
    success_url= reverse_lazy('Lista')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'post']
class BorrarPost(DeleteView):
    model = Post
    template_name = "borrarpost.html"
    success_url= reverse_lazy('Lista')
class NuevoPost(CreateView):
    model = Post
    template_name = "nuevopost.html"
    fields = '__all__'
def agregarPost(request):
    if request.method == "POST":
        usuario = request.user
        form = PostForm(request.POST)
        form.autor = usuario.id
        form.fecha = timezone.now
        form.imagen = 'default.jpeg'
        if form.is_valid():
            form.save()
            return redirect(to='Lista')
        else:
            return render(request,"error.html", {"mensaje":form.errors})
    else:
        form = PostForm()
        return render(request, "nuevopost.html", {"form":form})



