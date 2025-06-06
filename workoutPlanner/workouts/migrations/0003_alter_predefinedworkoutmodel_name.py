# Generated by Django 5.1.3 on 2024-12-14 10:18

import django.core.validators
import workoutPlanner.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_customworkoutmodel_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predefinedworkoutmodel',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), workoutPlanner.validators.AlphaNumericValidator('Workout name must contain letters and numbers only!')]),
        ),
    ]
