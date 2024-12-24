# Generated by Django 5.1.3 on 2024-12-15 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_predefinedworkoutmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predefinedworkoutmodel',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]