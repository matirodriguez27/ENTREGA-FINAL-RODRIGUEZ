from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse_lazy

class ListaPosts(ListView):
    model = Post
    template_name="listaposts.html"
class DetallePost(DetailView):
    model = Post
    template_name="detallepost.html"
class NuevoPost(CreateView):
    model = Post
    success_url = reverse_lazy('lista')
    fields = ['titulo', 'subtitulo', 'autor', 'cuerpo', 'fecha', 'post']
class EditarPost(UpdateView):
    model = Post
    success_url= reverse_lazy('lista')
    fields = []
class BorrarPost(DeleteView):
    model = Post
    success_url= reverse_lazy('lista')

