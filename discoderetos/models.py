from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

###############   DIFICULTAD    #################

class Dificultad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Dificultad', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Activada/Desactivada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'dificultad'
        verbose_name_plural = 'dificultades'

    def __str__(self):
        return self.nombre



###############   CATEGORIA    #################

class CategoriaReto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Categoria Reto', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre



###############   CHALLENGE    #################

class Challenge(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 150, blank = False, null = False)
    instrucciones = RichTextField('Instrucciones')
    thumbnail = models.URLField(max_length = 510, blank = False, null = False)
    dificultad = models.ForeignKey(Dificultad, on_delete = models.CASCADE)
    categoria = models.ForeignKey(CategoriaReto, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'challenge'
        verbose_name_plural = 'challenges'
        ordering = ['-id']

    def __str__(self):
        return self.titulo