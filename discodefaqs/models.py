from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
###############   FAQS    #################

class CategoriaFAQ(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Faqs(models.Model):
    id = models.AutoField(primary_key = True)
    pregunta = models.CharField('Pregunta?', max_length = 90, blank = False, null = False)
    respuesta = RichTextField('Respuesta')
    categoria = models.ForeignKey(CategoriaFAQ, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'faq'
        verbose_name_plural = 'faqs'

    def __str__(self):
        return self.pregunta