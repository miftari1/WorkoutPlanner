# Generated by Django 5.1.3 on 2024-12-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('technique', models.TextField()),
                ('muscle_groups', models.CharField(choices=[('QP', 'Quadriceps'), ('HS', 'Hamstring'), ('SH', 'Shoulder'), ('TP', 'Triceps'), ('BP', 'Biceps'), ('FA', 'Forearm'), ('GM', 'Gluteus maximus'), ('CV', 'Calves'), ('CT', 'Chest'), ('BK', 'Back'), ('AB', 'Abs')], max_length=2)),
                ('image', models.ImageField(upload_to='exercises_images/')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'db_table': 'exercises_exercisemodel',
            },
        ),
    ]
