# Generated by Django 5.1.3 on 2024-11-28 22:21

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_alter_exercisemodel_muscle_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisemodel',
            name='muscle_groups',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('QP', 'Quadriceps'), ('HS', 'Hamstring'), ('SH', 'Shoulder'), ('TP', 'Triceps'), ('BP', 'Biceps'), ('FA', 'Forearm'), ('GM', 'Gluteus maximus'), ('CV', 'Calves'), ('CT', 'Chest'), ('BK', 'Back'), ('AB', 'Abs')], max_length=30),
        ),
    ]
