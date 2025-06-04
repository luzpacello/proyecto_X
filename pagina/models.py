from django.db import models

# Create your models here.
class Publicacion(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    id_img = models.CharField(max_length=2083, default='sin_imagen')

    def __str__(self):
        return self.name

    def imagen_url_directa(self):
        return f'https://drive.google.com/thumbnail?id={self.id_img}'

