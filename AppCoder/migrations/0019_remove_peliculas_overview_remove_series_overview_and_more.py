# Generated by Django 4.2.5 on 2023-09-05 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_alter_peliculas_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculas',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='series',
            name='overview',
        ),
        migrations.AddField(
            model_name='peliculas',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]