from django import forms

from workoutPlanner.workouts.models import PredefinedWorkoutModel


class PredefinedWorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = PredefinedWorkoutModel
        fields = '__all__'