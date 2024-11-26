from django.db import models
from django.utils.text import slugify

from workoutPlanner.exercises.choices import MuscleGroupChoices


class ExerciseModel(models.Model):
    class Meta:
        app_label = 'exercises'
        db_table = 'exercises_exercisemodel'

    name = models.CharField(max_length=255)

    overview = models.TextField()
    technique = models.TextField()
    muscle_groups = models.CharField(
        max_length=2,
        choices=MuscleGroupChoices
    )
    image = models.ImageField(upload_to='exercises_images/')
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
