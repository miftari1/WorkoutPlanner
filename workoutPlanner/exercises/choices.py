from django.db import models

class MuscleGroupChoices(models.TextChoices):
    QP = 'QP', 'Quadriceps'
    HS = 'HS', 'Hamstring'
    SH = 'SH', 'Shoulder'
    TP = 'TP', 'Triceps'
    BP = 'BP', 'Biceps'
    FA = 'FA', 'Forearm'
    GM = 'GM', 'Gluteus maximus'
    CV = 'CV', 'Calves'
    CT = 'CT', 'Chest'
    BK = 'BK', 'Back'
    AB = 'AB', 'Abs'