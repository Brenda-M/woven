# Generated by Django 3.0.7 on 2020-06-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200612_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pictures'),
        ),
    ]
