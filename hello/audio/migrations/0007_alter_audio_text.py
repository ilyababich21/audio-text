# Generated by Django 4.0.5 on 2022-06-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0006_audio_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
