from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    estado = models.BooleanField('Activo/No Activo', default = True)
    image = models.ImageField(default = 'profile.png')

    class Meta:
            verbose_name = 'Perfil'
            verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def following(self):
        user_ids = Relationship.objects.filter(from_user = self.user)\
            .values_list('to_user_id', flat = True)

        return User.objects.filter(id__in = user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user = self.user)\
            .values_list('from_user_id', flat = True)

        return User.objects.filter(id__in = user_ids)


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


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]