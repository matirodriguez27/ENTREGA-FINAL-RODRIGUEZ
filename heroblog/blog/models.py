from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
class Posteo(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    cuerpo = models.TextField()
    fecha = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.titulo
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.imagen.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.imagen.path)
        