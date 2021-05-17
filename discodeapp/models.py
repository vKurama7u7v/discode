from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

###############   BLOG    #################

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Autor', max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos de Autor', max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    linkedin = models.URLField('LinkedIn', null = True, blank = True)
    web = models.URLField('Sitio Web', null = True, blank = True)
    correo = models.EmailField('Correo Electronico', null = False, blank = False)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 200, blank = False, null = False)
    contenido = RichTextField('Contenido')
    thumbnail = models.URLField(max_length = 510, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    keywords = models.TextField('Palabras Clave (500 Carácteres)', max_length = 500, null = True, blank = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-id']

    def __str__(self):
        return self.titulo



