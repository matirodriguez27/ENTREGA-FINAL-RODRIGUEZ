from email.policy import default
from django import forms
from .models import Posteo, User
from django.db import models
from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):
    titulo = forms.CharField(max_length=250)
    subtitulo = forms.CharField(max_length=250)
    cuerpo = RichTextFormField()
    imagen = forms.ImageField(widget=forms.FileInput())
    fecha = models.DateTimeField()
    autor = forms.CharField()
    class Meta:
        model = Posteo
        fields = ['autor','titulo', 'subtitulo', 'cuerpo','imagen']