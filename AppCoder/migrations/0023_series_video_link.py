# Generated by Django 4.2.5 on 2023-09-05 19:20

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0022_peliculas_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='video_link',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
