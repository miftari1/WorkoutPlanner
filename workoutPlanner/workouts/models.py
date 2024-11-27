from django.db import models

from workoutPlanner.exercises.models import ExerciseModel


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
    exercises = models.ManyToManyField(
        ExerciseModel,
        related_name='predefined_workout_exercises',
    )
    overview = models.TextField()
    content = models.TextField()
    workout_manual = models.TextField()
    effects = models.TextField()
    extra_info = models.TextField(blank=True,  null=True)

    def __str__(self):
        return self.name
