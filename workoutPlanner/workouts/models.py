from django.db import models
from django.utils.text import slugify

from workoutPlanner.exercises.models import ExerciseModel
from workoutPlanner.workouts.choices import FitnessLevelChoices, TrainingTypeChoices


class CustomWorkoutModel(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(
        ExerciseModel,
    related_name='custom_workout_exercises',
    )

    def __str__(self):
        return self.name


class PredefinedWorkoutModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        max_length=150,
        blank=True)
    exercises = models.ManyToManyField(
        ExerciseModel,
    )
    level = models.CharField(max_length=2,
                             choices=FitnessLevelChoices,
                             default=None)
    training_type = models.CharField(max_length=3,
                                     choices=TrainingTypeChoices,
                                     )
    overview = models.TextField()
    content = models.TextField()
    workout_manual = models.TextField()
    effects = models.TextField()
    extra_info = models.TextField(blank=True,  null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
