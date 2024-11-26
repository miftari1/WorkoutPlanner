from django import forms

from workoutPlanner.exercises.models import ExerciseModel


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = ExerciseModel
        exclude = ['slug']