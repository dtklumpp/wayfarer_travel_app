# Generated by Django 3.1.2 on 2020-10-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20201009_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_image/default_profile_photo.svg', upload_to='profile_image'),
        ),
    ]
