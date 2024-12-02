from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.db import models
from django.utils.text import slugify

from workoutPlanner.accounts.models import Profile
from workoutPlanner.exercises.models import ExerciseModel
from workoutPlanner.workouts.choices import FitnessLevelChoices, TrainingTypeChoices


class CustomWorkoutModel(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="custom_workout",
        primary_key=True,
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        max_length=150,
        blank=True)
    exercises = models.ManyToManyField(
        ExerciseModel,
    related_name='custom_workout_exercises',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CustomWorkoutExerciseModel(models.Model):
    workout = models.ForeignKey(
        CustomWorkoutModel,
        on_delete=models.CASCADE,
        related_name='custom_exercises',
    )
    exercise = models.ForeignKey(
        ExerciseModel,
        on_delete=models.CASCADE,
        related_name='custom_exercise',
    )
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    rest = models.PositiveSmallIntegerField()


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
