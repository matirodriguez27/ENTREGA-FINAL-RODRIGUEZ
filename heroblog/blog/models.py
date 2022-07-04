from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.autor.username