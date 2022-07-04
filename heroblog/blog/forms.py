from email.policy import default
from django import forms
from .models import Post
from django.utils import timezone
class PostForm(forms.ModelForm):
    titulo = forms.CharField(max_length=250)
    subtitulo = forms.CharField(max_length=250)
    cuerpo = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'cuerpo','imagen']