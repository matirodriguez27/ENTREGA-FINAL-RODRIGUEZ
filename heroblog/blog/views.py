from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Posteo
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaPosts(ListView):
    model = Posteo
    template_name="listaposts.html"
class DetallePost(DetailView):
    model = Posteo
    template_name="detallepost.html"
    fields = ['autor','titulo', 'subtitulo', 'cuerpo','imagen']
class EditarPost(UpdateView):
    model = Posteo
    template_name = "editarpost.html"
    fields = ['titulo', 'subtitulo', 'cuerpo','imagen']
    success_url= reverse_lazy('Lista')
class BorrarPost(DeleteView):
    model = Posteo
    template_name = "borrarpost.html"
    success_url= reverse_lazy('Lista')
class NuevoPost(LoginRequiredMixin, CreateView):
    model = Posteo
    template_name = "nuevopost.html"
    success_url= reverse_lazy('Lista')
    fields = ['titulo', 'subtitulo', 'cuerpo','imagen']
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
