# Generated by Django 4.2.4 on 2023-08-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_delete_usuario_rename_genero_peliculas_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='genero',
        ),
        migrations.AddField(
            model_name='peliculas',
            name='genero',
            field=models.ManyToManyField(to='AppCoder.generos'),
        ),
    ]
