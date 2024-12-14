from django import forms
from django.forms import inlineformset_factory

from workoutPlanner.workouts.models import CustomWorkoutModel, CustomWorkoutExerciseModel

CustomWorkoutExerciseFormSet = inlineformset_factory(
    parent_model=CustomWorkoutModel,
    model=CustomWorkoutExerciseModel,
    fields=['exercise', 'sets', 'reps', 'rest'],
    extra=1,
    widgets={
        'exercise': forms.Select(attrs={'readonly': True}),
        'sets': forms.NumberInput(attrs={'placeholder': 'Sets'}),
        'reps': forms.NumberInput(attrs={'placeholder': 'Reps'}),
        'rest': forms.NumberInput(attrs={'placeholder': 'Rest'})
    },
    labels={'exercise': '',
            'sets': '',
            'reps': '',
            'rest': ''},
        )

UpdateCustomWorkoutExerciseFormSet = inlineformset_factory(
    parent_model=CustomWorkoutModel,
    model=CustomWorkoutExerciseModel,
    fields=['exercise', 'sets', 'reps', 'rest'],
    extra=1,
    widgets={
        'exercise': forms.Select(),
        'sets': forms.NumberInput(attrs={'placeholder': 'Sets'}),
        'reps': forms.NumberInput(attrs={'placeholder': 'Reps'}),
        'rest': forms.NumberInput(attrs={'placeholder': 'Rest'})
    },
    labels={'exercise': '',
            'sets': '',
            'reps': '',
            'rest': ''},
        )
