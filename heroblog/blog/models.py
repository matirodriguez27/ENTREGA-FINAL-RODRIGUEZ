from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    post = models. ImageField(upload_to='posts')

    def __str__(self):
        return self.title