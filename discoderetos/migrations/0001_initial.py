# Generated by Django 3.1.7 on 2021-05-05 04:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaReto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Categoria Reto')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria no Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Dificultad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Dificultad')),
                ('estado', models.BooleanField(default=True, verbose_name='Activada/Desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'dificultad',
                'verbose_name_plural': 'dificultades',
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('instrucciones', ckeditor.fields.RichTextField(verbose_name='Instrucciones')),
                ('thumbnail', models.URLField(max_length=510)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discoderetos.categoriareto')),
                ('dificultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discoderetos.dificultad')),
            ],
            options={
                'verbose_name': 'challenge',
                'verbose_name_plural': 'challenges',
            },
        ),
    ]
