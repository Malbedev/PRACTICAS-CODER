# Generated by Django 4.2.4 on 2023-08-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_peliculas_destacada'),
    ]

    operations = [
        migrations.AddField(
            model_name='directores',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directores',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
