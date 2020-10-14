# Generated by Django 3.1.2 on 2020-10-14 16:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20201011_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='user.png', max_length=255, verbose_name='image'),
        ),
    ]