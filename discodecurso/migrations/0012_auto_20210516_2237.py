# Generated by Django 3.1.7 on 2021-05-16 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discodecurso', '0011_auto_20210510_0256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['-id'], 'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]