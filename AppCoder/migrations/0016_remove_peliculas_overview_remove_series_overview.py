# Generated by Django 4.2.4 on 2023-09-03 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_alter_series_slug'),
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
    ]