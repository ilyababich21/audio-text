# Generated by Django 4.0.5 on 2022-06-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_alter_audio_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(upload_to='audio/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]
