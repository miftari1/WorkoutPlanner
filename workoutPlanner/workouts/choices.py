from django.db import models


class FitnessLevelChoices(models.TextChoices):
    B = 'B', 'Beginner'
    A = 'A', 'Advanced'
    I = 'I', 'Intermediate'


class TrainingTypeChoices(models.TextChoices):
    ST = 'ST', 'Strength Training'
    HIT = 'HIT',  'HIIT'
    CT = 'CT', 'Circuit Training'
    BT = 'BT', 'Bodyweight Training'

