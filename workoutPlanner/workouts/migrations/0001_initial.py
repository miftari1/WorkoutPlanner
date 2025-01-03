# Generated by Django 5.1.3 on 2024-12-05 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomWorkoutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_workout', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='CustomWorkoutExerciseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveSmallIntegerField()),
                ('reps', models.PositiveSmallIntegerField()),
                ('rest', models.PositiveSmallIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_exercises', to='exercises.exercisemodel')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_exercises', to='workouts.customworkoutmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PredefinedWorkoutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('A', 'Advanced'), ('I', 'Intermediate')], default=None, max_length=2)),
                ('training_type', models.CharField(choices=[('ST', 'Strength Training'), ('HIT', 'HIIT'), ('CT', 'Circuit Training'), ('BT', 'Bodyweight Training')], max_length=3)),
                ('overview', models.TextField()),
                ('content', models.TextField()),
                ('workout_manual', models.TextField()),
                ('effects', models.TextField()),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('exercises', models.ManyToManyField(to='exercises.exercisemodel')),
            ],
        ),
    ]
