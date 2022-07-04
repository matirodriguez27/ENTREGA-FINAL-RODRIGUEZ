from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        nuevoPost = Post
        model = nuevoPost
        fields = ('titulo', 'subtitulo', 'cuerpo')