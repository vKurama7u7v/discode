# Generated by Django 3.1.7 on 2021-05-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discodesocial', '0002_auto_20210510_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.URLField(default='https://cdn.glitch.com/27131a37-2b0c-4505-85fd-e4cd33d55125%2F1783805.jpg?v=1614832688191'),
        ),
    ]
