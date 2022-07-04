from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse_lazy 
from .forms import PostForm

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
def nuevoPost(request):
    if request.method == "POST":
        form = PostForm(data = request.POST)
        form.autor = self.request.usuario
        if form.is_valid():
            form.save()
            return redirect('Lista')
        else:
            return render(request,"error.html", {"mensaje":"Formulario invalido"})
    else:
        form = PostForm()
        return render(request, "nuevopost.html", {"form":form})

