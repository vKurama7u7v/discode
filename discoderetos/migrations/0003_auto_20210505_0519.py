# Generated by Django 3.1.7 on 2021-05-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discoderetos', '0002_challenge_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='descripcion',
            field=models.CharField(max_length=150, verbose_name='Descripcion'),
        ),
    ]
