# Generated by Django 3.1.7 on 2021-05-05 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discodecurso', '0005_auto_20210505_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leccion',
            old_name='slugleccion',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='slugtema',
            new_name='slug',
        ),
    ]