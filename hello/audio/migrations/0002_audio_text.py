# Generated by Django 4.0.5 on 2022-06-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='text',
            field=models.FileField(default=1, upload_to='text/'),
            preserve_default=False,
        ),
    ]
