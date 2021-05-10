from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    estado = models.BooleanField('Activo/No Activo', default = True)
    # image =

    class Meta:
            verbose_name = 'Perfil'
            verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Publicacion(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    fecha_creacion = models.DateTimeField(default = timezone.now)
    estado = models.BooleanField('Activo/No Activo', default = True)
    contenido = models.TextField()

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f'{self.user.username}: {self.contenido}'