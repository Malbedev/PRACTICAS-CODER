# Generated by Django 4.2.5 on 2023-09-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0019_remove_peliculas_overview_remove_series_overview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
