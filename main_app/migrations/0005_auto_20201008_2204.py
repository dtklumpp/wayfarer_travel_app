# Generated by Django 3.1.2 on 2020-10-08 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201008_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('city', models.CharField(choices=[('SF', 'San Francisco'), ('LD', 'London'), ('GB', 'Gibraltar')], default='SF', max_length=2)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.post')),
            ],
        ),
    ]
