from django.db import models

class MuscleGroupChoices(models.TextChoices):
    QP = 'QP', 'Quadriceps'
    HS = 'HS', 'Hamstring'
    FD = 'FD', 'Front deltoids'
    SD = 'SD', 'Side deltoids'
    RD = 'RD', 'Rear deltoids'
    TP = 'TP', 'Triceps'
    BP = 'BP', 'Biceps'
    FA = 'FA', 'Forearm'
    GM = 'GM', 'Gluteus maximus'
    CV = 'CV', 'Calves'
    CT = 'CT', 'Chest'
    BK = 'BK', 'Back'
    AB = 'AB', 'Abdominals'