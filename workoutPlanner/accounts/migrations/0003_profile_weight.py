# Generated by Django 5.1.3 on 2024-11-20 21:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1, error_messages='Weight cannot be negative number.', validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
