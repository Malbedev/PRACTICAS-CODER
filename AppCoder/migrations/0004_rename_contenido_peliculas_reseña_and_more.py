# Generated by Django 4.2.4 on 2023-08-24 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_generos_remove_peliculas_genero_peliculas_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peliculas',
            old_name='contenido',
            new_name='reseña',
        ),
        migrations.AlterField(
            model_name='directores',
            name='filmografia',
            field=models.ManyToManyField(blank=True, to='AppCoder.peliculas'),
        ),
        migrations.CreateModel(
            name='Curadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apeliido', models.CharField(max_length=50)),
                ('reseñas', models.ManyToManyField(blank=True, to='AppCoder.peliculas')),
            ],
        ),
        migrations.AddField(
            model_name='peliculas',
            name='autor_reseña',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.curadores'),
        ),
    ]
