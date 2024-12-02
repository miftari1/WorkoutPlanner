from django import forms
from django.forms import inlineformset_factory

from workoutPlanner.workouts.models import PredefinedWorkoutModel, CustomWorkoutModel


class PredefinedWorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = PredefinedWorkoutModel
        fields = '__all__'

class CustomWorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = CustomWorkoutModel
        fields = ['name']
