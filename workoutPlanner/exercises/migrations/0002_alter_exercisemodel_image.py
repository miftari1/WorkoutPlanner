# Generated by Django 5.1.3 on 2024-11-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisemodel',
            name='image',
            field=models.ImageField(upload_to='exercises_images/'),
        ),
    ]
