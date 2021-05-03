# Generated by Django 3.1.7 on 2021-04-25 06:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discodeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discodeapp.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion',
            field=models.CharField(default=1, max_length=200, verbose_name='Descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Publicado/No Publicado'),
        ),
        migrations.AddField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=100, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discodeapp.autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=90, verbose_name='Titulo'),
        ),
    ]
