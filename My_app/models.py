from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(default='default.jpg', upload_to='post_pics')
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
