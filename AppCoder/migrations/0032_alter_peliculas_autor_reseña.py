# Generated by Django 4.2.4 on 2023-09-20 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0031_alter_peliculas_autor_reseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='autor_reseña',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
