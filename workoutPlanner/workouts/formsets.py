from django import forms
from django.forms import inlineformset_factory

from workoutPlanner.workouts.models import CustomWorkoutModel, CustomWorkoutExerciseModel

CustomWorkoutExerciseFormSet = inlineformset_factory(
    parent_model=CustomWorkoutModel,
    model=CustomWorkoutExerciseModel,
    fields=['exercise', 'sets', 'reps', 'rest'],
    extra=1,
    can_delete=True,
    widgets={'exercise': forms.Select(attrs={'disabled': True}),}
)