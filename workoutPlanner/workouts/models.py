from django.core.serializers import serialize
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from workoutPlanner.accounts.models import Profile
from workoutPlanner.exercises.models import ExerciseModel
from workoutPlanner.validators import AlphaNumericValidator
from workoutPlanner.workouts.choices import FitnessLevelChoices, TrainingTypeChoices


class CustomWorkoutModel(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="custom_workouts",
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        max_length=150,
        blank=True)

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
        related_name='custom_exercises',
    )
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    rest = models.PositiveSmallIntegerField()


class PredefinedWorkoutModel(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator('Workout name must contain letters and numbers only!')
        ])
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
