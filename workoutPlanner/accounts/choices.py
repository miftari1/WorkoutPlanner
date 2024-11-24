from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    M = 'M', _('Male')
    F = 'F', _('Female'),


class GoalChoices(models.TextChoices):
    FL = 'FL', _('Fat Loss'),
    M = 'M', _('Maintenance'),
    MG = 'MG', _('Muscle Gain'),


class ActivityChoices(models.TextChoices):
    LA = 'LA', _('Lightly Active (workouts not often with sedentary job)'),
    MA = 'MA', _('Moderately Active (workouts often with sedentary job)'),
    VA = 'VA', _('Very Active (workouts not often with active job)'),
    EA = 'EA', _('Extremely Active (workouts often with active job)'),

