from django import forms
from django.forms import inlineformset_factory

from workoutPlanner.workouts.models import PredefinedWorkoutModel, CustomWorkoutModel


class PredefinedWorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = PredefinedWorkoutModel
        exclude = ['slug']
        widgets = {}

class CustomWorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = CustomWorkoutModel
        fields = ['name']
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Workout name'}),
        }
        labels={'name':''
        }
