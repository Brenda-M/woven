# Generated by Django 3.0.7 on 2020-06-11 18:57

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200611_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='average',
            field=models.DecimalField(decimal_places=1, default=20.0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
