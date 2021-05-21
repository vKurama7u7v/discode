from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

###############   CATEGORIA CURSO    #################

class CategoriaCurso(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Categoria Curso', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


###############   CURSO    #################

class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    thumbnail = models.URLField(max_length = 510, blank = False, null = False)
    categoria = models.ForeignKey(CategoriaCurso, on_delete = models.CASCADE)

    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['-id']

    def __str__(self):
        return self.titulo


###############   TEMA    #################
class Tema(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Tema', max_length = 100, blank = False, null = False)
    identificador = models.ForeignKey(Curso, on_delete = models.CASCADE)
    estado = models.BooleanField('Visible/No Visible', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'temas'

    def __str__(self):
        return self.titulo


###############   LECCION    #################
class Leccion(models.Model):
    id = models.AutoField(primary_key = True)
    subtitulo = models.CharField('Lección', max_length = 100, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    identificador = models.ForeignKey(Tema, on_delete = models.CASCADE)
    
    contenido = RichTextField('Contenido del Tema')
    codigo = models.TextField('Codigo', blank = True, null = True)

    estado = models.BooleanField('Visible/No Visible', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'leccion'
        verbose_name_plural = 'lecciones'

    def __str__(self):
        return self.subtitulo
